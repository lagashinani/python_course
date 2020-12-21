from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding="cp1251") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)


def get_cell(cell_num):
    groups = re.search(cell_pattern, cell_num)
    result_num = ""

    # если что-то нашел в этом поле по такому шаблону
    if (groups is not None):
        # выделяет найденные группы
        groups = groups.groups()
        # если есть номер и есть добавочный в пятой группе
        if (len(groups) > 4 and groups[4] is not None):
            result_num = "+7({}){}-{}-{} доб.{}".format(*groups[0:5])

        # если есть номер и есть добавочный в шестой группе
        elif (len(groups) > 4 and groups[5] is not None):
            result_num = "+7({}){}-{}-{} доб.{}".format(*groups[0:4], groups[5])
        # нет добавочного
        else:
            result_num = "+7({}){}-{}-{}".format(*groups[0:4])

    return result_num

def is_similar(f, s):
    # считает метрику похожести двух контактов
    res = 0
    for v1, v2 in zip(f, s):
        if (v1 != v2 and v1 != "" and v2 != ""):
            res += 1
    return res < 1

def union_it(f, s):
    # дополняет пустые поля первого из второго
    for i in range(len(f)):
        if (f[i] == ""):
            f[i] = s[i]
    return f

cell_pattern = "(\d{3})\D{0,2}(\d{3})\D{0,1}(\d{2})\D{0,1}(\d{2})(?:$|,(\d+)|\D+(\d+))"
fio_pattern = "([\w-]*)\s*([\w-]*)\s*([\w-]*)"

contacts_dict = {}

for i, contact in enumerate(contacts_list[1:], 1):
    # хоть что-то неправильно заполнено
    if (contact[0] == "" or contact[1] == "" or contact[2] == ""):
        concat = contact[0] + " " + contact[1] + " " + contact[2]
        fio_gr = re.search(fio_pattern, concat)
        fio_res = []
        if (fio_gr is not None):
            fio_res = fio_gr.groups()
            contacts_list[i][0] = fio_res[0]
            contacts_list[i][1] = fio_res[1]
            contacts_list[i][2] = fio_res[2]

            
    cell_num = get_cell(contact[5])
    if (cell_num != ""):
        contacts_list[i][5] = cell_num

    similars = contacts_dict.get(contacts_list[i][0] + "\t" + contacts_list[i][1])
    if (similars is not None):
        # есть совпадение, проверим его побольше
        for similar_i in range(len(similars)):
            if is_similar(contacts_list[i], similars[similar_i]):
                # обьединяем
                similars[similar_i] = union_it(similars[similar_i], contacts_list[i])
                break
        else:
            # если так ни с кем и не обьединили, то добавляем как новый контакт
            similars.append(contacts_list[i])
    else:
        # если нет похожих, то заводим новый список на эту фамилию-имя
        similars = [contacts_list[i]]
    # обновляем список граждан на эту фамилию-имя
    contacts_dict[contacts_list[i][0] + "\t" + contacts_list[i][1]] = similars

head = contacts_list[0]
contacts_list = sorted([contact for sim_contacts in contacts_dict.values() for contact in sim_contacts])

with open("phonebook.csv", "w", newline='') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerow(head)
    datawriter.writerows(contacts_list)