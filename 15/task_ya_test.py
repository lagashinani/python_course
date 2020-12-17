import unittest
from unittest.mock import patch
import requests

from ya import YAApi
token = "AgAAAAA4fkDBAADLW7K3AC0P8UjniibQMr5xU0k"
path = "photos_test"

class TestYaApi(unittest.TestCase):

    def test0_really_exists(self):
        self.api = YAApi(token)
        response_dir = requests.get("https://cloud-api.yandex.net/v1/disk/resources", 
                headers={"Authorization": "OAuth " + token,
                         "Content-Type": "application/json"},
                params={"path": path})
        self.assertEqual(response_dir.status_code, 404)

    def test1_success_code(self):
        self.api = YAApi(token)
        # создаст пустую папку
        response = self.api.save_to_yandex(path, [])[1]
        self.assertEqual(response.status_code, 201)
        self.assertTrue('href' in response.json())
        self.assertEqual(response.json()['href'], 
            "https://cloud-api.yandex.net/v1/disk/resources?path=disk%3A%2Fphotos_test")

    def test2_folder_exists(self):
        self.api = YAApi(token)
        response = self.api.save_to_yandex(path, [])[1]
        self.assertEqual(response.status_code, 409)
        self.assertTrue('error' in response.json())
        self.assertEqual(response.json()['error'], 
            "DiskPathPointsToExistentDirectoryError")

    def test3_really_exists(self):
        self.api = YAApi(token)
        response_dir = requests.get("https://cloud-api.yandex.net/v1/disk/resources", 
                headers={"Authorization": "OAuth " + token,
                         "Content-Type": "application/json"},
                params={"path": path})
        self.assertEqual(response_dir.status_code, 200)




if __name__ == '__main__':
    unittest.main()