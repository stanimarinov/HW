# Задача 2. Напишете програма, която показва знака (+ или -) от частното на две реални числа, 
# без да го пресмята.

x = float(input(" "))
y = float(input(" "))
result = x / y
if result > 0:
    print("+")
if result < 0:
    print("-")
