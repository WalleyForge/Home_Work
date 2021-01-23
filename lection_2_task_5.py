list1 = [7, 5, 3, 3, 2]
ls = list1.copy()
while True:
    user = input("Укажите номер рейтинга, для выхода нажмите q: ")
    try:
        if str(user)== "q":
            break
        if user != "q" or user != int:
            int(user)
    except ValueError:
            print("Введите целое число: ")
    else:
        user = int(user)
        for i in range(len(ls)):
            if ls[i] == user:
                ls.insert(i, user)
                break
            elif ls[0] < user:
                ls.insert(i, user)
                break
            elif ls[-1] > user:
                ls.append(user)
                break
            elif ls[i] < user and ls[i-1] > user:
                ls.insert(i, user)
        print(f"Начальный тир лист: {list1}")
        print(f"Новый результат тир листа: {ls}")
