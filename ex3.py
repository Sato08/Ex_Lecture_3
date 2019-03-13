data = ["newfile.txt", "photoshop.psd", "word.docx"]
result = []

for char in data:
	for value in char:
		if(value == "."):
			index = char.index(value)
			result.append(char[:index])
print(result, end = " ")