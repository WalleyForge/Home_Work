"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. 
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
 К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, atribut):
        self.atribut = atribut


    @property
    def consumption(self):
        cloths =  f'Сумма затраченной ткани равна: {self.atribut / 6.5 + 0.5 + 2 * self.atribut + 0.3}'
        return cloths

    @abstractmethod
    def abstract(self):
        abstract = ""
        return abstract

class Coat(Clothes):
    def consumption(self):
        coats = f"Для пошива пальто нужно: {self.atribut / 6.5 + 0.5} ткани"
        return coats
    
    def abstract(self):
        abstract = ""
        return abstract
 

class Costume(Clothes):
    def consumption(self):
        costum = f"Для пошива костюма нужно: {2* self.atribut + 0.3} ткани"
        return costum
    
    def abstract(self):
        abstract = ""
        return abstract


c = Coat(100)
s = Costume(500)
print(c.consumption())
print(s.consumption())
print(c.abstract())
