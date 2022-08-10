import uvicorn
from fastapi import FastAPI
from routers import get_photo, likes_photo

app = FastAPI()

app.include_router(get_photo.router)
app.include_router(likes_photo.router)

uvicorn.run(app, host='0.0.0.0', port=8080)


