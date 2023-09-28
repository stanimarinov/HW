# Задача 6. Да се напише програма, която да сортира списък
# от tuples използвайки Lambda, (използвайки вторите елементи на tuples)


lot = [
	(1,2),
	(1,1),
	(4,3),
	(2,0)
]
lot_sorted = sorted( lot, key=lambda t:t[1])
print( lot_sorted )