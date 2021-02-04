# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

with open("sky.txt", "w") as files:
    print("Укажите строку слов и нажмите Enter, после введите пустую строку и нажмите Enter")
    texts = input("Укажите текст: ")
    while texts:
        files.writelines(texts)
        texts = input("Укажите текст: ")
        if texts == " ":
            break

    files = open("sky.txt", "r")
    content = files.readlines()
    print(content)


