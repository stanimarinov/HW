#5. Да се състави програма, която да изчислява периметър и площ на
#правоъгълник по въведени дължини на прилежащи страни - естествени числа от
#интервала [5 ..100]. Изведете съобщение, ако страните формират квадрат.
#Използвайте проверка на логическо условие - оператор if.

a = int(input("Въведете страна a: "))
b = int(input("Въведете страна b: "))
P = 2*(a + b)
S = a * b
if a == b :
    print("Квадрат", "Лице",(S), "Периметър",(P))
else :
    print("Лице",(S), "Периметър",(P))    
