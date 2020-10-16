import requests
from progress_bar import my_progress_bar


class YAApi():
    def __init__(self, token):
        self.ya_token = token


    def save_to_yandex(self, path, photos):
        '''Загружает файлы из photos на яндекс диск'''
        # создаем папку
        response = requests.put("https://cloud-api.yandex.net/v1/disk/resources", 
                headers={"Authorization": "OAuth " + self.ya_token,
                         "Content-Type": "application/json"},
                params={"path": path})
        # print(response.json())

        names = set()
        results = []
        print("Uploading to YA drive")
        for photo in my_progress_bar(photos):
            name = str(photo[1])
            if (photo[1] in names):
                name += "_"
                name += str(photo[0])

            names.add(name)

            response = requests.post("https://cloud-api.yandex.net/v1/disk/resources/upload", 
                headers={"Authorization": "OAuth " + self.ya_token,
                         "Content-Type": "application/json"},
                params={"path": path + "/" + name + ".jpg", 
                        "url": photo[2]})

            results.append({"file_name": name + ".jpg", "size": photo[3]})

        return results