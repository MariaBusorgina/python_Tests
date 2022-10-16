import requests


class Yandex_user:
    def __init__(self, name_folder, token):
        self.name_folder = name_folder
        self.token = token
        self.URL = 'https://cloud-api.yandex.net/v1/disk/resources'

    def new_folder(self):
        HEADERS = {"Authorization": f'OAuth {self.token}'}
        folder_param = {
            'path': self.name_folder
        }

        response = requests.put(self.URL, params=folder_param, headers=HEADERS)
        return response.status_code


