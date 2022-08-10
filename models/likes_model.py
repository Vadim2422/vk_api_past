import json

import requests

from auth_data import token_5707 as token, apiV
from models.base_model import BaseModel
from models.photo_model import Photo

str = f"https://api.vk.com/method/likes.add?type=photo&item_id=457253221&access_token={token}&v={apiV}"
print(str)


class LikesAllPhoto(BaseModel):
    def __init__(self, type, owner_id):
        super().__init__()
        self.owner_id = owner_id
        self.type = type

    def likes_all_photo(self, items_id):
        for item in items_id:
            url = f"https://api.vk.com/method/likes.add?type={self.type}&owner_id={self.owner_id}&item_id={item}&access_token={token}&v={apiV}"
            requests.get(url)

    def delete_likes_all_photo(self, items_id):
        for item in items_id:
            url = f"https://api.vk.com/method/likes.delete?type={self.type}&owner_id={self.owner_id}&item_id={item}&access_token={token}&v={apiV}"
            requests.get(url)

    @staticmethod
    def get_items_id(data):
        items_id = []
        for item in data['response']['items']:
            items_id.append(item['id'])
        return items_id
