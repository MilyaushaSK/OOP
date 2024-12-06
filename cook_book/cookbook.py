# Создаем словарь из данных файла
with open('recipes.txt', 'rt', encoding = "utf-8") as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        dish_ing = [] 
        ing_num = file.readline()  
        for _ in range(int(ing_num)):
            element = file.readline()
            ingredient_name, quantity, measure  = element.strip().split(' | ')
            dish_ing.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
                })
        empty_line = file.readline()
        cook_book[dish_name] = dish_ing     

print(f'cook_book = {cook_book}')

# Создаем словарь с названием ингредиентов и его количества для блюда
def get_shop_list_by_dishes(dishes, person_count):
    ing_quantity = {}
    for dish in dishes:
        if dish in cook_book.keys():
           for ingradient in cook_book[dish]:
               ingredient_name = ingradient['ingredient_name']
               quantity = ingradient['quantity']
               measure = ingradient['measure']
               overall_quantity = int(quantity) * person_count
               if ingredient_name in ing_quantity:
                    ing_quantity[ingredient_name]['quantity'] += overall_quantity
               else: 
                    ing_quantity[ingredient_name] = {'measure': measure, 
                                                     'quantity': overall_quantity}
    return ing_quantity

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))


