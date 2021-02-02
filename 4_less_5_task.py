# 5. Реализовать формирование списка, используя функцию range() и возможности генератора. 
# В список должны войти четные числа от 100 до 1000 (включая границы).
#  Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().


from functools import reduce

def alef(a,b):
    return a * b


even_number = [el for el in range(99, 1001) if el % 2 == 0]
print(f"Список четных чисел: {even_number}")
alls = reduce(alef, [el for el in range(99, 1001) if el % 2 == 0])
print(f"Итог: {alls}")

