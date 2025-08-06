#Prime Numbers

number = int(input('Enter a number to check if it is a prime number:\n'))

total_divisors = 0

for check in range(1, number +1):
	if number % check == 0:
		total_divisors += 1
		
if total_divisors == 2:
	print(f'The number {number} is a Prime Number')
else:
	print(f'The number {number} is not a prime number!')