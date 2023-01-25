from setuptools import find_packages, setup

setup(
    name="data_pipelines",
    packages=find_packages(exclude=["data_pipelines_tests"]),
    install_requires=[
        "fastapi",
        "pydantic",
        "sqlalchemy",
        "psycopg2",
        "alembic",
        "uvicorn",
        "python-jose[cryptography]",
        "passlib[bcrypt]",
        "python-multipart"

    ],
    extras_require={"dev": ["black", "isort", "ruff"]},
)
