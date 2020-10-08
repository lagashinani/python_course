import requests

token = ""


def get_int_of(name):
    # делаем запрос
    response = requests.get("https://superheroapi.com/api/" + token + "/search/" + name).json()
    # если запрос успешен и он для нашего героя, то возвращаем его интеллект из ответа
    # print(response)
    if (response["response"] == "success" and response["results-for"] == name):
        return response["results"][0]["powerstats"]["intelligence"]
    return None


heros = ["Hulk", "Captain America", "Thanos"]
# для каждого героя вызываем нашу функцию
heros_int = [(hero, int(get_int_of(hero))) for hero in heros]
# выбираем максимум по интеллекту
print(max(heros_int, key = lambda x: x[1])[0])