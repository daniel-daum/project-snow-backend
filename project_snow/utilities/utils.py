import smtplib
import ssl

from passlib.context import CryptContext
from sqlalchemy.orm import Session

from project_snow.database import schemas

from ..database import models
from ..settings import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash(password: str):
    return pwd_context.hash(password)


def verify(plain_password, hashed_password):

    return pwd_context.verify(plain_password, hashed_password)


# SENDS A VERIFICATION EMAIL WITH A LINK. LINK IS TO VERIFY EMAIL POST ROUTE AND INCLUDES A JWT


def send_verification_email(db: Session, token: str, user: schemas.User):

    URL = ""

    if settings.DEPLOYMENT_ENV == "development":
        URL = f"http://localhost:8000/api/auth/verify_email/{token}"

    if settings.DEPLOYMENT_ENV == "production":
        URL = (
            f"https://coral-app-gpjaj.ondigitalocean.app/api/auth/verify_email/{token}"
        )

    from email.message import EmailMessage

    # Pack user data and token string into a dict
    user_dict = {"users_id": user.id, "users_email": user.email, "temp_jwt": token}

    # Add dict data into table model
    temp_user_verification_info = models.Email_Verification(**user_dict)

    # AAdd user data to the database
    db.add(temp_user_verification_info)
    db.commit()

    # Generate and send an email to the user with verification information.
    msg = EmailMessage()

    msg["Subject"] = "Project Snow - Verify Your Email Address"
    msg["From"] = settings.EMAIL
    msg["To"] = user.email
    msg.set_content(
        f"""
    <html lang="en">
    <body style="font-family:Arial, Helvetica, sans-serif ;">
    <p>Hello, {user.first_name.title()}!</p>
    <p> Please click the button below to verify your email address and complete registration for Project Snow</p>
    <div>
        <p style="font-weight: 700; color:black; font-size:1em; padding: .3em;"><a href="{URL}" style="text-decoration: underline; color:black" >Verify Your Email Address</a></p>
    </div>
    <p>This email was sent to: {user.email.upper()}
        Please do not reply to this message.
        Project Snow will never contact you by email asking you to validate your personal information such as your password.
        
        If you recieve such a request please contact us at <span style="text-decoration:c underline ;">daniel_daum@outlook.com</span></p>
    </body>
    </html>
    """,
        subtype="html",
    )

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(settings.EMAIL_SERVER, 465, context=context) as smtp:
        smtp.login(settings.EMAIL, settings.EMAIL_SERVER_KEY)
        smtp.send_message(msg)
        smtp.quit()

    return
