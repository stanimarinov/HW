# Задача 7. Да се напише програма, която да сортира 
#списък от речници (by values) използвайки Lambda.

lod = [
	{'a': 3},
	{'b': 1},
	{'c': 2}
]
lod_sorted = sorted( lod, key=lambda d: list(d.values())[0] )
print(lod_sorted)