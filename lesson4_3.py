#   3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
#   Необходимо решить задание в одну строку.
#   Подсказка: использовать функцию range() и генератор.

listResult = [i for i in range(20, 241) if (i % 20) * (i % 21) == 0]
print(f"Результат : {listResult}")