#Задача 1. Дефинирайте клас Student, който съдържа следната информация за 
#студентите: трите имена, курс, специалност, университет, електронна поща и телефонен 
#номер.

class Student:
    def __init__(self, name, midle_name, last_name, course, specialty, university, email, tel):
        self.name = name
        self.midlename = midle_name
        self.lastname = last_name
        self.course = course
        self.specialty = specialty
        self.university = university
        self.email = email
        self.tel = tel
