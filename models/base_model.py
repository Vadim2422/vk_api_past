import json
import requests
from auth_data import fake_token as token, apiV


class BaseModel:
    def __init__(self):
        self.token = token

    @staticmethod
    def get_id(user_id):
        url = f'https://api.vk.com/method/users.get?user_ids={user_id}&fields=id&access_token={token}&v={apiV}'
        return json.loads(requests.get(url).text)['response'][0]['id']
