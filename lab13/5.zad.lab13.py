#Задача 5. Модифицирайте текущия код на класа Student така, че да капсулирате данните 
#в класа чрез свойства.

class Student:
    def __init__(self, name="", mname = None, lname = "", course = 0, specialty = "", university = "", email = "", tel = 0):
        self._name = name
        self._midlename = mname
        self._lastname = lname
        self._course = course
        self._specialty = specialty
        self._university = university
        self._email = email
        self._tel = tel

    @property
    def tel(self):
        return self._tel

    @tel.setter
    def tel(self,new_tel):
        self._tel = new_tel
    
std1 = Student("Petar","Petrov") 
std2 = Student("Ivan","Ivanov")  

std1.tel = 1234
print(std1._tel)
