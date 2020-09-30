
with open("recipes.txt", encoding="utf-8") as o:
    read = o.read().split("\n\n")

cook_book = {}
for dish in read: 
    lines = dish.split("\n")
    
    cook_book[lines[0]] = []
    for line in lines[2:]:
        cook_book[lines[0]].append({'ingredient_name': line.split(" | ")[0],
                                  'quantity': line.split(" | ")[1],
                                  'measure': line.split(" | ")[2]
                                  })

# print(cook_book)

def get_shop_list_by_dishes(dishes, person):
    shop_list = {}
    for dish in dishes:
        for ingr in cook_book[dish]:
            if (ingr['ingredient_name'] not in shop_list):
                shop_list[ingr['ingredient_name']] = {"measure": ingr["measure"], 
                                                      "quantity": int(ingr['quantity']) * person}
            else:
                shop_list[ingr['ingredient_name']]["quantity"] += int(ingr['quantity']) * person


    return shop_list


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))







