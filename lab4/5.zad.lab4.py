# Задача 5. Напишете програма, която при въвеждане на коефициентите (a, b и c) на квадратно
# уравнение ax^2+bx+c изчислява и извежда неговите реални корени. 


a = float (input("Въведи коефицент a: "))
b = float (input("Въведи коефицент b: "))
c = float (input("Въведи коефицент c: "))
discriminant = b**2 - 4*a*c
if discriminant > 0 :
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Квадратното уравнение има два реални корена:")
    print(f"Корен 1 : {root1}")
    print(f"Корен 2 : {root2}")
elif discriminant == 0 :
    root = -b / (2*a)
    print(f"Квадратното уравнение има един реален корен:")
    print(f"Корен : {root}")  
else :
    print("Квадратното уравнение няма реални корени.")