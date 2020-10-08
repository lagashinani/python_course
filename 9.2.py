with open("newsafr.xml", encoding="utf8") as inp:
    xml = inp.read()




xml_spl = []
while True:
    st1 = xml.find("<item ")
    if (st1 == -1):
        break
    st1 = xml.find(">", st1)
    st2 = xml.find("</item>")
    
    xml_spl.append({})

    xml_dict_now = xml[st1+1: st2]

    while True:
        key_1 = xml_dict_now.find("<")
        if (key_1 == -1):
            break
        key_2 = xml_dict_now.find(">", key_1 + 1)

        val_2 = xml_dict_now.find("<", key_2 + 1)

        xml_spl[-1][xml_dict_now[key_1 + 1:key_2]] = xml_dict_now[key_2 + 1:val_2]
        xml_dict_now = xml_dict_now[val_2 + 1:]

    xml = xml[st2 + 1:]


words_count = {}
for rec in xml_spl:
    words = (rec["description"] + " " + rec["title"]).split()
    for word in words:
        if len(word) > 6:
            words_count[word] = words_count.get(word, 0) + 1


print(sorted(words_count.items(), key=lambda x: x[1], reverse=True)[:10])
