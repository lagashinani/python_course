with open("newsafr.json", encoding="utf8") as inp:
    json = inp.read()

# открываем файл и выделяем часть, которая отвечает за новости - "items": [...]

start = json.find("\"items\": [") + 10
stop = json.find("]", start)
json = json[start: stop]
json = json.replace("\n", "")

json_spl = []

while True:
    # выделяем строку, содержающую очередной словарь, отвечающий за конкретную новость
    st1 = json.find("{")
    if (st1 == -1):
        break
    st2 = json.find("}")
    
    json_spl.append({})
    
    # кладем строку со словарем сюда
    json_dict_now = json[st1+1: st2]
    while True:
        # для каждой записи из словаря выделяем ключ и значение и кладем в словарь, удаляя из исходной строки
        key_1 = json_dict_now.find("\"")
        if (key_1 == -1):
            break
        key_2 = json_dict_now.find("\"", key_1 + 1)

        val_1 = json_dict_now.find("\"", key_2 + 2)
        val_2 = json_dict_now.find("\"", val_1 + 1)

        json_spl[-1][json_dict_now[key_1 + 1:key_2]] = json_dict_now[val_1 + 1:val_2]
        json_dict_now = json_dict_now[val_2 + 1:]
    
    json = json[st2 + 1:]

words_count = {}
# для каждой новости берем описание и название, склеиваем и делим на слова
for rec in json_spl:
    words = (rec["description"] + " " + rec["title"]).split()
    # считаем каждое слово
    for word in words:
        if len(word) > 6:
            words_count[word] = words_count.get(word, 0) + 1


print(sorted(words_count.items(), key=lambda x: x[1], reverse=True)[:10])


# способ с помощью парсера

import json
with open("newsafr.json", encoding="utf8") as inp:
    json_r = json.load(inp)

json_spl = json_r['rss']['channel']["items"]
words_count = {}
for rec in json_spl:
    words = (rec["description"] + " " + rec["title"]).split()
    for word in words:
        if len(word) > 6:
            words_count[word] = words_count.get(word, 0) + 1
print(sorted(words_count.items(), key=lambda x: x[1], reverse=True)[:10])










