#Задача 8. Да се принтира буквата A на екрана както е дадено по-долу:
#  *** 
# *   * 
# *   * 
# ***** 
# *   * 
# *   * 
# *   * 

top = 3
midle = 5
rows = 2*midle - 4

for row in range(rows):
    if row==0:
        print(" ", "*" * 3 , " " , sep="")
    if row==2:
        print("*" * 5)    
    else :
        print("*" , " " * top , "*" , sep="")