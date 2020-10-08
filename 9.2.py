import xml.etree.ElementTree as etree



def extract_info_from_xml(file_name):
    '''Отвечает за работу с xml api:
        file_name: имя файла
        return: список словарей из названий и тела новостей'''
    tree = etree.parse(file_name)
    root = tree.getroot()
    items = root.findall("channel")[0].findall("item")
    return [{"title": item.find("title").text,  
             "description": item.find("description").text} for item in items]

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

xml_spl = extract_info_from_xml("newsafr.xml")
words_count = get_word_count(xml_spl, 6)
print(get_topn_words(words_count, 10))
