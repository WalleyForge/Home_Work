"""3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
 Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
 Класс-исключение должен контролировать типы данных элементов списка."""

class Mistake(ValueError): 

    def __init__(self, my_list):  
        self.my_list = []
    def ss(self):     
        while True:
            try:
                num = input('Введите число в список:')
                if num == 'q' or num == "Q": 
                    break
                if not num.isdigit():   
                    raise Mistake(num)     
                self.my_list.append(int(num)) 
            except Mistake as Exception:  
                print("Для выхода введите Q")
                print('Нужно число, попробуйте еще раз')
        print(f"Текущий список {self.my_list}")


a = Mistake(1)
a.ss()
