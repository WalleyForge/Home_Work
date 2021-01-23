# Реализовать функцию, принимающую два числа
# (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.


def alef(user, user1):
    try:
        delet = user / user1
    except ValueError:
        print("Укажите число: ")
    except ZeroDivisionError:
        print("К сожалению, на ноль делить нельзя, попробуйте еще раз: ")
    else:
        return delet

player = float(input("Введите первое число: "))
player2 = float(input("Введите 2 число:"))

print(f"Результат: {player} / {player2} = {alef(player,player2)}")

