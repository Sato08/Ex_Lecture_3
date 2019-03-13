import string
data = ["python", "patience", "documents", "students", "homework",
 "practice", "success", "english", "university", "congratulation"]
alp = string.ascii_lowercase

results = []
sum_value = 0
for word in data:
	for char in word:
		sum_value += alp.index(char) + 1
	print(word," : ", sum_value)

'''python  :  98
patience  :  171
documents  :  285
students  :  407
homework  :  515
practice  :  590
success  :  679
english  :  753
university  :  915
congratulation  :  1085'''