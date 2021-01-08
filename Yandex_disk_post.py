import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файл file_path на яндекс диск"""
        self.file_path = file_path
        resp1 = requests.get(
            "https://cloud-api.yandex.net/v1/disk/resources/upload",
            params={"path": "/file.json", "overwrite": "true"},
            headers=self.token
        )
        resp1.raise_for_status()
        d = resp1.json()
        href = d["href"]

        with open(file_path, "rb") as f:
            resp2 = requests.put(href, files={"file": f})
        resp2.raise_for_status()

        print('Файл успешно загружен')


if __name__ == '__main__':
    uploader = YaUploader({"Authorization": "OAuth <Your Yandex Disk token>"})
    result = uploader.upload('c:\my_folder\file.json')
