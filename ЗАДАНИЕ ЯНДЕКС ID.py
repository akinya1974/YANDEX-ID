
import requests, os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):

        file_path = os.path.normpath(file_path)
        header = {"Authorization" : f'OAuth {self.token}'}
        file = {"file": open(file_path, 'rb')}

        response_url = requests.get(
        "https://cloud-api.yandex.net/v1/disk/resources/upload",
        params = {"path": file_path},
        headers = header)
        url = response_url.json().get('href')

        response_upload = requests.put(url, files = file, headers = {})
        return print(response_upload.status_code)


if __name__ == '__main__':
    uploader = YaUploader(token)
    result = uploader.upload("file to upload/")
