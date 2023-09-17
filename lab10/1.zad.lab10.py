#Задача 1. Да се напише програма, която да реализира генератор на четни числа

evens = list(range(2,11,2))
evens = [el for el in range(2,11) if el%2==0]
print(evens)