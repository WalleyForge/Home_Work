# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.


spisoc = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
spisoc1 = []
with open("sky4.txt", "r") as files:
    for i in files:
        i = i.split(" ", 1)
        spisoc1.append(spisoc[i[0]] + " " + i[1])
    print(spisoc1)

with open("sky4_1.txt", "w") as files:
    files.writelines(spisoc1)