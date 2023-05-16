import requests
from pprint import pprint
def zadacha1():
    result = {}
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url)
    for i in response.json():
        if i['name'] == 'Hulk':
            result['Hulk'] = i['powerstats']['intelligence']
        if i['name'] == 'Captain America':
            result['Captain America'] = i['powerstats']['intelligence']
        if i['name'] == 'Thanos':
            result['Thanos'] = i['powerstats']['intelligence']
    max_ = max(result, key=result.get)
    print(f'Самый умный герой - {max_}')


class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        print(response.status_code)
        pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        print(response.status_code)
        if response.status_code == 201:
            print("Success")


ya = YandexDisk(token="")
ya.upload_file_to_disk("test/test.txt", "test.txt")