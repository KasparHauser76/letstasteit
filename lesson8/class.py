# задание 1
class Animals:
    """Класс животных имеет признаки:
       пол, возраст, количество конечностей, наличие шерсти, 
       наличие крыльев, наличие жабр, хищничество.
    """
    def init(self, gender, age, 
                number_of_limbs, wool, wings, 
                gills, predation):
        self.gender = gender
        self.age = age
        self.number_of_limbs = number_of_limbs
        self.wool = wool
        self.wings = wings
        self.gills = gills
        self.predation = predation

class Mammals(Animals):
    """Класс млекопитающих описывает те же признаки, что и животные + вскармливание детенышей молоком"""
    def init(self, gender, age, number_of_limbs, 
                wool, wings, gills, predation, nursing_milk):
        super().init(gender, age, number_of_limbs, wool, wings, gills, predation)
        self.nursing_milk = nursing_milk
    

class Human(Mammals):
    """Класс людей наследует все признаки млекапитающих + имя, рост, вес, речь"""
    def init(self, gender, age, number_of_limbs, wool, wings, gills, 
                predation, nursing_milk, height, weight, name, speech):
        super().init(gender, age, number_of_limbs, 
                        wool, wings, gills, predation, nursing_milk)
        self.height = height
        self.weight = weight
        self.name = name
        self.speech = speech


class Cat(Mammals):
    """Класс кошачьих наследуют все признаки млекопитающих + имя, окрас, ночное зрение"""
    def init(self, gender, age, number_of_limbs, 
                wool, wings, gills, predation, nursing_milk,
                name, color, night_vision):
        super().init(gender, age, number_of_limbs, 
                wool, wings, gills, predation, nursing_milk)
        self.name = name
        self.color = color
        self.night_vision = night_vision

class Dog(Mammals):
    """Класс собаки наследует все признаки млекопитающих + кличка, порода"""
    def init(self, gender, age, number_of_limbs, wool, wings, gills,
                predation, nursing_milk, nickname, breed):
        super().init(gender, age, number_of_limbs, wool, wings, gills, 
                        predation, nursing_milk)
        self.nickname = nickname
        self.breed = breed

# Задание 2
class Student:
    """Класс студентов имеет все признаки людей + количество сданных дз"""
    def init(*args, self, gender, age, number_of_limbs, wool, wings, gills, 
                predation, nursing_milk, height, weight, name, speech, dz):
        super().init(gender, age, number_of_limbs, wool, wings, gills, 
                        predation, nursing_milk, height, weight, name, speech)
        self.dz = dz

#Задание 3

"""функции сравнения студентов по количеству сданных дз
   путем перегрузки ператоров
"""

def lt(self, another):
    self_dz = self.dz
    another_dz = another.dz
    return self_dz < another_dz

def le(self, another):
    self_dz = self.dz
    another_dz = another.dz
    return self_dz <= another_dz

def eq(self, another):
    self_dz = self.dz
    another_dz = another.dz
    return self_dz == another_dz

def ne(self, another):
    self_dz = self.dz
    another_dz = another.dz
    return self_dz != another_dz

def gt(self, another):
    self_dz = self.dz
    another_dz = another.dz
    return self_dz > another_dz

def ge(self, another):
    self_dz = self.dz
    another_dz = another.dz
    return self_dz >= another_dz

# пример для сравнения будет выглядеть примерно так
        
print('Введите данные студентов')
print('Для первого студента')
Student_1 = Student(input('Пол: '), input('Возраст: '), 'Yes', 'No', 'No', 'No', 'Yes', 'Yes', input('Рост: '), input('Вес: '), input('Имя: '), 'Yes', input('Количество сданных ДЗ: '))
print('Для второго студента')
Student_2 = Student(input('Пол: '), input('Возраст: '), 'Yes', 'No', 'No', 'No', 'Yes', 'Yes', input('Рост: '), input('Вес: '), input('Имя: '), 'Yes', input('Количество сданных ДЗ: '))

if Student_1 == Student_2:
    print('У студентов одинаковое количество выполненых ДЗ')
if Student_1 < Student_2:
    print(f'{Student_1.name} сделал меньше ДЗ чем {Student_2.name}')
if Student_1 > Student_2:
    print(f'{Student_1.name} сделал больше ДЗ чем {Student_2.name}')
if Student_1 >= Student_2:
    print(f'У студентов одинаковое количество выполненых работ или {Student_1.name} сделал больше чем {Student_2.name}')
if Student_1 <= Student_2:
    print(f'У студентов одинаковое количество выполненых работ или {Student_1.name} сделал меньше чем {Student_2.name}')

# на оставшееся задание с декораторами, прошу простить, в связи с рождением ребенка, времени катастрофически не хватило :) 