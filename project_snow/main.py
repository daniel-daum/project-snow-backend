from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from project_snow.settings import settings

from .routes import auth, resorts, users, weather

app = FastAPI(title="Project Snow", version="0.0.0")

if settings.DEPLOYMENT_ENV == "development":

    URL: str = "https://www.localhost:8000/"

else:
    URL: str = "https://stingray-app-rg8ve.ondigitalocean.app/"

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(resorts.router)
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(weather.router)


# root
@app.get("/")
async def root():
    """Returns a link to the API documentation"""

    return {"Root": f"API documentation is located at {URL + 'docs'}"}
