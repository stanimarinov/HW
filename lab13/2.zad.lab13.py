#Задача 2. Декларирайте конструктор за класа Student, които да инициализира всички 
#атрибути на класа. Данните за полетата, които не са известни трябва да се 
#инициализират съответно със стойности с None, 0, или “”.

class Student:
    def __init__(self, name="", midle_name = None, last_name = "", course = 0, specialty = "", university = "", email = "", tel = 0):
        self.name = name
        self.midlename = midle_name
        self.lastname = last_name
        self.course = course
        self.specialty = specialty
        self.university = university
        self.email = email
        self.tel = tel

std1 = Student("Petar","Petrov") 
std2 = Student("Ivan","Ivanov")  
