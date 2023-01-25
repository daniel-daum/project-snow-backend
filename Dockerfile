FROM python:3.10

WORKDIR /usr/src/app

# COPY requirements.txt ./

RUN pip install \
    fastapi \
    pydantic \
    sqlalchemy \
    psycopg2 \
    alembic \
    python-dotenv \
    uvicorn \
    python-jose[cryptography] \
    passlib[bcrypt]

COPY . .

EXPOSE 8080

CMD ["uvicorn", "project_snow.main:app", "--host", "0.0.0.0", "--port", "8080"]
