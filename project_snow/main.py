from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes import auth, resorts, users

app = FastAPI(title="Project Snow", version="0.0.0")

URL: str = "https://www.localhost:8000/"

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


# root
@app.get("/")
async def root():
    """Returns a link to the API documentation"""

    return {"Root": f"API documentation is located at {URL + 'docs'}"}
