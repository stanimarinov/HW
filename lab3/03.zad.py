# Задача 3. Създайте стринг, filename и му присвоете стойност “hello.py”. 
# Проверете дали стринга завършва на “.java”. Намерете индексът на ”py”. 
# Проверете и дали думата започва с ”world”.

filename = "hello.py"
print( filename.endswith(".java") )
print(filename.find(".py"))
print(filename.startswith("world"))