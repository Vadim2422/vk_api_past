import shutil
from fastapi import APIRouter
from fastapi.responses import FileResponse
from models.photo_model import Photo

router = APIRouter(prefix='/photo', tags=['photo'])
path = 'foto'


@router.get("/get_all/{user_id}", response_class=FileResponse)
async def get_photo(user_id: str, offset=0):
    Photo.delete()
    get = Photo(user_id)
    photos = get.photo_200(offset)
    count = photos['response']['count']
    links = Photo.links_from_json(photos)
    while count - 200 > 0:
        offset += 200
        links.extend(Photo.links_from_json(get.photo_200(offset)))

        count -= 200

    Photo.download_photo(links, path)
    shutil.make_archive("archive", 'zip', "foto")

    return FileResponse(path="archive.zip")
