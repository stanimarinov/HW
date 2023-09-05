# Задача 5. Напишете програма, която да премахва ”$$” от името ”$$John Smith”. Опитайте с 
# .lstrip и .strip(). За да видите описанието на двете функции използвайте следното help(“ ”.strip).

user_name = "$$John Smith"
print( user_name.strip("$"))
print( user_name.lstrip("$"))