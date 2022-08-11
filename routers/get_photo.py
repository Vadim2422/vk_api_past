import shutil
from fastapi import APIRouter
from fastapi.responses import FileResponse
from models.photo_model import Photo

router = APIRouter(prefix='/photo', tags=['photo'])
path = 'foto'


@router.get("/get_all/{user_id}", response_class=FileResponse)
async def get_photo(user_id: str):
    Photo.delete()
    links = Photo.get_all_photo(user_id)
    Photo.download_photo(links, path)
    shutil.make_archive("archive", 'zip', "foto")

    return FileResponse(path="archive.zip")
