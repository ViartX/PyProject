# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

# функция принимает строку и возвразает число слов в строке
def get_words_number_in_string(str):
    str_list = str.split()
    return len(str_list)


f_text = open("lesson5_2.txt", 'r')
str_num = 0
for line in f_text:
    str_num += 1
    print(f"   слов в строке {str_num} : {get_words_number_in_string(line)}")
print(f"строк в файле : {str_num}")

f_text.close()