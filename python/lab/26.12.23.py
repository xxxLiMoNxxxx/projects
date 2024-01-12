import random

numbers = []
numbers_len = random.randint(1,10)
count_plus = 0
count_minus = 0
count_zero = 0
for i in range(0, numbers_len+1):
    n = random.randint(-100, 100)
    numbers. append(n)
    if (n <= -1):
        count_minus += 1
    elif (n >= 1):
        count_plus += 1
    elif (n == 0):
        count_zero += 1

print (numbers)
print(min(numbers))
print(max(numbers) )
print (f"Додатних = {count_plus} ")
print (f"Відємних = {count_minus} ")
print (f"Нулів = {count_zero} ")