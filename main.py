import uvicorn
from fastapi import FastAPI

import auth
from routers import get_photo, likes_photo, main
from utils import get_hashed_password

app = FastAPI()

app.include_router(get_photo.router)
app.include_router(likes_photo.router)
app.include_router(auth.router)
app.include_router(main.router)




uvicorn.run(app, host='0.0.0.0', port=8080)


