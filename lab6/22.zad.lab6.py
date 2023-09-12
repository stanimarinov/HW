# Задача 22. Да се напише програма, която да принтира буквата D:

top = 4
rows = 7

for row in range(rows):
    if row==0:
        print("*" * 4)
    if row==6:
        print("*" * 4)    
    else: 
        print("*", " "*3, "*" ) 
         