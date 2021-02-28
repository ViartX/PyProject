# list - element type ------------------------------------------------------------------
my_list1 = [1, "dva", bool("True"), 4.1]
for i in range(len(my_list1)):
    print(f"Элемент {i} со значением {my_list1[i]} имеет тип {type(my_list1[i])}")
print()

# list values exchange -----------------------------------------------------------------
my_list2 = []
list_len = int(input("введите длину списка : "))

# iterating till the range
for i in range(0, list_len):
    list_element = int(input(f"введите элемент №{i+1}' : "))
    my_list2.append(list_element)
print(f"лист в начале: {my_list2}")

i = 0
while i < list_len-1:
    temp = my_list2[i+1]
    my_list2[i+1] = my_list2[i]
    my_list2[i] = temp
    i = i + 2

print(f"лист в конце: {my_list2}")
print()

# months ---------------------------------------------------------------------------------
seasons_list = ["Зима", "Зима", "Весна", "Весна", "Весна", "Лето", "Лето", "Лето", "Лето", "Осень", "Осень", "Осень", "Зима"]
seasons_dict = {1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна", 6: "Лето", 7: "Лето", 8: "Лето", 9: "Осень", 10: "Осень", 11: "Осень", 12: "Зима"}

i = int(input("введите номер месяца : "))
if 0 < i < 13:
    print(f"seasons_list говорит что это: {seasons_list[i]}")
    print(f"seasons_dict говорит что это: {seasons_dict.get(i)}")
print()

# string --------------------------------------------------------------------------------
string = (input("введите строку : "))
string_list = string.split()
for i in range (0, len(string_list)):
    temp_string = string_list[i][0:10]
    print(f"{i:} {temp_string}")
print()

# rating --------------------------------------------------------------------------------
my_list3 = [7, 5, 3, 3, 2]
my_list3.sort(reverse = True)
print(f"лист в начале: {my_list3}")
new_value = int(input("введите новое число : "))
# цикл для вставки в нужное место нового числа
for i in range(0, len(my_list3)):
    if new_value >= my_list3[i]:
        my_list3.insert(i,new_value)
        break
# если число не вставлено так как самое маленькое, добавляем его в конец
if my_list3[len(my_list3)-1] > new_value:
    my_list3.append(new_value)

print(f"лист в конце: {my_list3}")
print()

# goods --------------------------------------------------------------------------------
spec = ["название", "цена", "количество", "ед"]
i_list = 0  # счетчик для списка кортежей
list = []

while True:
    # условие выхода из цикла
    action = input("Ввести новый товар? (Да/Нет) :")
    if action.upper() == "НЕТ":
        break

    # создаем и наполняем словарь
    new_dict = {}
    for i in range(0, len(spec)):
        new_value = input(f"введите {spec[i]} :")
        new_dict[spec[i]] = new_value

    # создаем и добавляем в списко кортеж
    new_tuple = (i_list, new_dict)
    list.append(new_tuple)
    i_list =+ 1

# вывод состояния списка для отладки
print(f"исходная структура: {list}")

anlt_dict = {}

for i in range(0, len(spec)):       # цикл по перечню полей
    anlt_list = []
    for j in range(0, len(list)):        # цикл по списку котрежей
        tuple = list[j]
        dict = tuple[1]
        value = dict.get(spec[i])
        anlt_list.append(value)
    anlt_dict[spec[i]] = anlt_list

# вывод состояния списка для отладки
print(f"итоговая структура: {anlt_dict}")





