import requests
import json
import time

from vk import VKApi
from ya import YAApi
from gd import GDApi
from od import ODApi

vk_token = ""
ya_token = ""

        


user = ""
album = "profile"

od_user_id = ""

vk_dir_name = user
od_dir_name = od_user_id


vkapi = VKApi(vk_token)
yaapi = YAApi(ya_token)
gdapi = GDApi()
odapi = ODApi()


vk_photos_links = vkapi.get_photos_links(vkapi.get_id(user), album_id=album, count=10)
od_photos_links = odapi.get_photos_links(od_user_id, count=2)

vk_saved = VKApi.save_photos(vk_dir_name, vk_photos_links)
od_saved = ODApi.save_photos(od_dir_name, od_photos_links)

ya_saved = yaapi.save_to_yandex("vk_" + user + "_" + album, vk_photos_links)
# print(list(map(lambda x: x["file_name"], od_saved)))
gdapi.upload_dir(od_dir_name, list(map(lambda x: x["file_name"], od_saved)))



with open("saved_photos_to_ya.json", "w+") as out:
    json.dump(vk_saved, out)