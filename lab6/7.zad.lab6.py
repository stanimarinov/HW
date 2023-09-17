#Задача 7. Да се напише програма, която принтира редицата на Фибуначи между 0 и 50.
#Редицата на Фибуначи е: 0, 1, 1, 2, 3, 5, 8, 13, 21, … Всяко следващо число е сумата от 
#предходните две. 


def make_fib_list(limit):

	l = []
	n1,n2 = 0,1
	while n2<limit:
		l.append(n2)
		n1, n2 = n2, n1+n2
	return l

fib_list = make_fib_list(50)
for num in fib_list:
	print(num, end=', ')