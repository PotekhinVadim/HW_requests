import requests
from settings import TOKEN

class YaUploader:
    def __init__(self, token: str):
        self.token = token
        self.HOST = 'https://cloud-api.yandex.net'
    
    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}

    def upload(self, file_path):
        uri = '/v1/disk/resources/upload'
        url = self.HOST + uri
        file_name = file_path.split("/")[-1]
        params = {'path': file_name, 'overwrite': 'true'}
        upload_link = requests.get(url, headers=self.get_headers(), params=params)
        response = requests.put(upload_link.json()['href'], headers=self.get_headers(), data=open(file_path, 'rb'))

if __name__ == '__main__':
    path_to_file = r'.....'
    uploader = YaUploader(TOKEN)
    result = uploader.upload(path_to_file)