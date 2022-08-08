from fastapi import FastAPI
from routers import get_photo

app = FastAPI()

app.include_router(get_photo.router)





