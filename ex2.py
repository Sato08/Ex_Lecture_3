results = []
for i in range(1, 101):
	if i % 15 == 0:
		results.append("FizzBuzz")
	elif i % 3 == 0:
		results.append("Buzz")
	elif i % 5 == 0:
		results.append("Fizz")
print(results, end = " ")
'''['Buzz', 'Fizz', 'Buzz', 'Buzz', 'Fizz', 'Buzz', 'FizzBuzz', 'Buzz', 'Fizz', 'Buzz', 'Buzz', 'Fizz', 'Buzz', 
'FizzBuzz', 'Buzz', 'Fizz', 'Buzz', 'Buzz', 'Fizz', 'Buzz', 'FizzBuzz', 'Buzz', 'Fizz', 'Buzz', 'Buzz',
 'Fizz', 'Buzz', 'FizzBuzz', 'Buzz', 'Fizz', 'Buzz', 'Buzz', 'Fizz', 'Buzz', 'FizzBuzz', 'Buzz', 'Fizz',
 'Buzz', 'Buzz', 'Fizz', 'Buzz', 'FizzBuzz', 'Buzz', 'Fizz', 'Buzz', 'Buzz', 'Fizz']'''