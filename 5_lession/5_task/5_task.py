# 5. Создать(программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


with open("sky5.txt", "w") as files:
    set_of_numbers = input("Введите числа: ")
    files.writelines(set_of_numbers)
    numbers = set_of_numbers.split()
    result = sum(map(int, numbers))
    print(f"Введенные числа: {set_of_numbers} \nИх сумма: {result}")
