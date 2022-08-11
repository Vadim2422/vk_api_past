from fastapi import APIRouter

from models.likes_model import LikesAllPhoto

router = APIRouter(prefix='/likes', tags=['likes'])


@router.get("/all_photo/{user_id}")
async def all_photo(user_id):
    items_id, owner_id = LikesAllPhoto.get_all_item_id(user_id)
    LikesAllPhoto('photo', owner_id).likes_all_photo(items_id)
    return "Successful"


@router.get("/delete_all_photo/{user_id}")
async def del_all_photo(user_id):
    items_id, owner_id = LikesAllPhoto.get_all_item_id(user_id)
    LikesAllPhoto('photo', owner_id).delete_likes_all_photo(items_id)
    return "Successful"
