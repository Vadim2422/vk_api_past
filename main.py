import uvicorn
from fastapi import FastAPI

from routers import get_photo, likes_photo, main, auth

app = FastAPI()

app.include_router(get_photo.router)
app.include_router(likes_photo.router)
app.include_router(auth.router)
app.include_router(main.router)


