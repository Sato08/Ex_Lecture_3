data = [[1, 2, 3], [4, 5], [6, [7, 8], 9], [10]]
result = []
for arr in data:
	for j in arr:
		if(type(j) == list):
			for t in j:
				result.append(t)
		else:
			result.append(j)
print("Platten list:", result, end = " ")

'''Platten list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]'''