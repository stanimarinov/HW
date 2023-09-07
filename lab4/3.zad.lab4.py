# Задача 3. Напишете програма, която намира най-голямото по стойност число, измежду три
# дадени числа. 

num1 = float (input (" Въведи първо число "))
num2 = float (input (" Въведи второ число "))
num3 = float (input (" Въведи трето число "))
if num1 > num2 and num1 > num3 :
    largest = num1
elif num2 > num1 and num2 > num3 :
    largest = num2
else :
    largest = num3  
    print (f" Най-голямото от въведените числа е: {largest}")  
