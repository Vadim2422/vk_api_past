from fastapi import APIRouter

from models.likes_model import LikesAllPhoto
from models.photo_model import Photo

router = APIRouter(prefix='/likes', tags=['likes'])


@router.get("/all_photo/{user_id}")
async def all_photo(user_id, offset=0):

    get = Photo(user_id)
    photos = get.photo_200(offset)
    count = photos['response']['count']
    items_id = LikesAllPhoto.get_items_id(photos)
    while count - 200 > 0:
        offset += 200
        items_id.extend(LikesAllPhoto.get_items_id(get.photo_200(offset)))
        count -= 200
    likes = LikesAllPhoto('photo', get.owner_id)
    likes.likes_all_photo(items_id)
    return "Successful"
