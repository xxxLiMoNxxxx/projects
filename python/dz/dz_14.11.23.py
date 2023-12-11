#Задача 1
print("\n Задача 1 \n")
def my_function():
    a = int(input("Введіть число: "))
    if (a >= 1001):
        print("Забагато, максимум 1000")
        return
    elif (a <= 0):
        print("Замало, мінімум 1")
        return
    sum = 0
    text = ''
    for i in range(1, a+1):
        if (i % 3 == 0 or i % 5 == 0):
            sum += i
            text += str(i) + ', '
    print(f"Сумма в діапозоні від 1 до {a} = {sum}")
    print("")
    if (sum == 0):
        print(f"Нічого не пройзходило, сумма ровна 0")
    else:
        print(f"Всі числа які кратні 3 та 5 у цьому діапозоні {text}")
my_function()
#Задача 2
print("\n Задача 2 \n")
a = int(input("Введіть число: "))
if a >= 0:
    for i in range(0,a+1):
        print(i)
else:
    for i in range(0,a-1,-1):
        print(i)
