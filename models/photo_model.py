import json
import os
import shutil
import requests
from auth_data import apiV
from models.base_model import BaseModel


class Photo(BaseModel):
    def __init__(self, owner_id):
        super().__init__()
        self.owner_id: int = BaseModel.get_id(owner_id)

    def photo_200(self, offset):
        url = f"https://api.vk.com/method/photos.getAll?owner_id={self.owner_id}&count=200&offset={offset}&access_token={self.token}&v={apiV} "
        return json.loads(requests.get(url).text)

    @staticmethod
    def links_from_json(data):
        links = []
        for photo in data['response']['items']:
            max_size = -1
            index_max_size = 0
            for index, size in enumerate(photo['sizes']):
                if size['height'] > max_size:
                    max_size = size['height']
                    index_max_size = index

            links.append(photo['sizes'][index_max_size]['url'])
        return links

    @staticmethod
    def download_photo(links, path):
        for i, link_photo in enumerate(links):
            img_file = open(path + f"/img{i + 1}.jpg", 'wb')
            img_file.write(requests.get(link_photo).content)
            img_file.close()

    @staticmethod
    def delete():
        if os.path.exists('foto'):
            shutil.rmtree('foto')
            os.mkdir('foto')
        if os.path.exists("archive.zip"):
            os.remove("archive.zip")



