import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загруджает файл file_path на яндекс диск"""

        with open(file_path, encoding="utf8") as inp:
            data = inp.read()

        # запрашиваем ссылку у яндекса для загрузки файла, с авторизацией и указанием имени файла
        response = requests.get("https://cloud-api.yandex.net/v1/disk/resources/upload", 
            headers={"Authorization": "OAuth " + self.token,
                     "Content-Type": "application/json"},
            params={"path": file_path, "overwrite": "true"})

        # если ссылка выдана (код 200) - загружаем наш файл по этой ссылке и возвращаем код ответа
        if (response.status_code == 200):
            response = requests.put(response.json()["href"], data=data.encode("utf8"))
            return response.status_code

        return 5000 + response.status_code

if __name__ == '__main__':
    uploader = YaUploader()
    file_path = input("Input file name")
    result = uploader.upload(file_path)
    print(result)