documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def print_docs_person():
    number = input("Enter doc ID: ")
    for doc in filter(lambda x: x["number"] == number, documents):
        print(doc['name'])

def print_docs_shelf():
    doc = input("Enter doc ID: ")
    for shelf, docs in directories.items():
        if (doc in docs):
            print(shelf)

def print_all_docs():
    res = []
    for doc in documents:
        print("{} \"{}\" \"{}\"".format(doc["type"], doc["number"], doc["name"]))
        res.append("{} \"{}\" \"{}\"".format(doc["type"], doc["number"], doc["name"]))
    return res

def add_doc():
    number = input("Enter doc ID: ")
    typ = input("Enter doc type: ")
    name = input("Enter name: ")
    shelf = input("Enter shelf number: ")

    while (shelf not in directories):
        print("No such shelf")
        shelf = input("Enter another shelf number: ")

    documents.append({"type": typ, "number": number, "name": name})
    directories[shelf].append(number)

def delete_doc():
    number = input("Enter doc ID: ")
    global documents
    documents = list(filter(lambda x: x['number'] != number, documents))

    for key in directories.keys():
        directories[key] = list(filter(lambda x: x != number, directories[key]))


def move_doc():
    number = input("Enter doc ID: ")
    shelf = input("Enter shelf num: ")

    check = False

    if shelf not in directories:
        print("No such shelf")
        return

    for key in directories.keys():
        temp = list(filter(lambda x: x != number, directories[key]))
        if (len(temp) != len(directories[key])):
            check = True
        directories[key] = temp

    if check:
        directories[shelf].append(number)
    else:
        print("No such doc")

def add_shelf():
    shelf = input("Enter shelf num: ")
    if (shelf not in directories):
        directories[shelf] = []
    else:
        print("Such shelf exists")

if __name__ == "__main__":
    while True:
        choice = input("Enter command e/p/s/l/a/d/m/as: ")
        if (choice == 'e'):
            break
        elif (choice == 'p'):
            print_docs_person()
        elif (choice == 's'):
            print_docs_shelf()
        elif (choice == 'l'):
            print_all_docs()
        elif (choice == 'a'):
            add_doc()
        elif (choice == 'd'):
            delete_doc()
        elif (choice == 'm'):
            move_doc()
        elif (choice == 'as'):
            add_shelf()

        else:
            print("Wrong Command")

