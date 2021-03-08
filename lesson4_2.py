# Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.


list1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
list2 = []
for i in range (1, len(list1)):
    if list1[i] > list1[i-1]:
        list2.append(list1[i])

list3 = [list1[i] for i in range(1, len(list1)) if list1[i] > list1[i-1]]

print(f"Исходный список   : {list1}")
print(f"Список из цикла   : {list2}")
print(f"Список генератора : {list3}")

