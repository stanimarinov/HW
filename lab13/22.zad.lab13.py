#Задача 22. Дадено ни е училище. В училището имаме класове и ученици. Всеки клас 
#има множество от преподаватели. Всеки преподавател има множество от дисциплини, 
#по които преподава. Учениците имат име и уникален номер в класа. Класовете имат 
#уникален текстов идентификатор. Дисциплините имат име, брой уроци и брой 
#упражнения. Трябва да декларирате класове заедно с техните полета, свойства, методи 
#и конструктори. Дефинирайте и тестов клас, който демонстрира, че останалите класове 
#работят коректно.


class Subject:
    def __init__(self, name, lesson_count, labs_count):
        self.name = name
        self.lesson_count = lesson_count
        self.labs_count = labs_count

class Clases:
    def __init__(self, txt_init):
        self.txt_init = txt_init

class Student:
    def __init__(self, name, class_number):
        self.name = name
        self.class_number = class_number

class Teachers:
    def __init__(self, subjects):
        self.subjects = subjects
        