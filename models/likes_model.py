

import requests

from auth_data import apiV
from models.base_model import BaseModel
from models.photo_model import Photo


class LikesAllPhoto(BaseModel):
    def __init__(self, type, owner_id):
        super().__init__()
        self.owner_id = owner_id
        self.type = type

    def likes_all_photo(self, items_id):
        for item in items_id:
            url = f"https://api.vk.com/method/likes.add?type={self.type}&owner_id={self.owner_id}&item_id={item}&access_token={self.token}&v={apiV}"
            print(url)
            requests.get(url)

    def delete_likes_all_photo(self, items_id):
        for item in items_id:
            url = f"https://api.vk.com/method/likes.delete?type={self.type}&owner_id={self.owner_id}&item_id={item}&access_token={self.token}&v={apiV}"
            requests.get(url)

    @staticmethod
    def get_items_id_200(data):
        items_id = []
        for item in data['response']['items']:
            items_id.append(item['id'])
        return items_id

    @staticmethod
    def get_all_item_id(user_id, offset=0):
        get = Photo(user_id)
        photos = get.photo_200(offset)
        count = photos['response']['count']
        items_id = LikesAllPhoto.get_items_id_200(photos)
        while count - 200 > 0:
            offset += 200
            items_id.extend(LikesAllPhoto.get_items_id_200(get.photo_200(offset)))
            count -= 200
        return items_id, get.owner_id
