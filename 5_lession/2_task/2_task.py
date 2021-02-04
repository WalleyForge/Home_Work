
with open("sky2.txt", "r") as files:
    content = files.read()
    print(f"Содержимое: {content.split()}")

    files = open("sky2.txt", "r")
    content = files.readlines()
    for i in range(len(content)):
        print(f"Кол-во строк: {i+1} Слов: {len(content[i])}")