#Задача 3. Добавете статично поле в класа Student, в което се съхранява броя на
#създадените обекти от този клас.

class Student:
    count = 0
    def __init__(self, name="", mname = None, lname = "", course = 0, specialty = "", university = "", email = "", tel = 0):
        self.name = name
        self.midlename = mname
        self.lastname = lname
        self.course = course
        self.specialty = specialty
        self.university = university
        self.email = email
        self.tel = tel
        Student.count = Student.count + 1



std1 = Student("Petar","Petrov") 
std2 = Student("Ivan","Ivanov")  