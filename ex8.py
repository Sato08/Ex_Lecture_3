data = [2, 3, 1, 5, 6, 8, 9, 10, 11, 21, 27, 0.12, 23.12, 36.01]
min_data = data[0]
max_data = data[0]

for value in data:
	if (value < min_data):
		min_data = value
	if (value > max_data):
		max_data = value

print("Min of data ", min_data, "Max of data: ", max_data)

'''Min of data  0.12 
Max of data:  36.01'''
