# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.


def my_func(user1,user2,user3):
    if user1 > user3 and user2 > user3:
        return user1 + user2
    elif user2 > user1 and user3 > user1:
        return user2 + user3
    elif user1 > user2 and user3 > user2:
        return user1 + user3

player1 = int(input("Введите первое число: "))
player2 = int(input("Введите второе число: "))
player3 = int(input("Введите третье число: "))

print(my_func(player1,player2,player3))