import json

def extract_info_from_json(file_name):
    '''Отвечает за работу с json api:
        file_name: имя файла
        return: список словарей из названий и тела новостей'''

    with open(file_name, encoding="utf8") as inp:
        json_r = json.load(inp)
    
    items = json_r['rss']['channel']["items"]
    
    return [{"title": item["title"],  
             "description": item["description"]} for item in items]

def get_word_count(items, min_len):
    '''Преобразует список словарей из названий и тел новостей в счетчик слов
       items: список словарей
       min_len: минимальная длина учитываемых слова
       return: словарь-счетчик'''
    words_count = {}
    for rec in items:
        words = (rec["description"] + " " + rec["title"]).split()
        for word in words:
            if len(word) > min_len:
                words_count[word] = words_count.get(word, 0) + 1
    return words_count

def get_topn_words(words_count, topn):
    '''Преобразует счетчик слов в спиок topn слов со счетчиком
       words_count: счетчик слов
       topn: количество top слов, для возврата
       return: список пар слово: количество'''
    return sorted(words_count.items(), key=lambda x: x[1], reverse=True)[:topn]


json_spl = extract_info_from_json("newsafr.json")
words_count = get_word_count(json_spl, 6)
print(get_topn_words(words_count, 10))






