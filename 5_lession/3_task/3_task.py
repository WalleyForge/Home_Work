# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. 
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. 
# Выполнить подсчет средней величины дохода сотрудников.
with open("sky3.txt", "r", encoding='utf-8') as files:
    lst = files.read().split('\n')
    employee = []
    average = []
    for i in lst:
        i = i.split()
        if int(i[1]) < 20000:
           employee.append(i[0])
        average.append(i[1])
print(f"Список сотрудников и их зп: {lst} ")
print(F"Список сотрудников, у кого меньше 20к зп: {employee}")
print(f"Среднаяя зарплата: {sum(map(int, average)) / len(average)} руб.")
