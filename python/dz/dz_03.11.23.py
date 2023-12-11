#Задача 1
while (True):
    quastion = int(input("Введіть цифру від 1 до 7: "))
    if (quastion == 1):
        print("Понеділок")
        break
    elif (quastion == 2):
        print("Вівторок")
        break
    elif (quastion == 3):
        print("Середа")
        break
    elif (quastion == 4):
        print("Четвер")
        break   
    elif (quastion == 5):
        print("П`ятниця")
        break
    elif (quastion == 6):
        print("Субота")
        break
    elif (quastion == 7):
        print("Неділя")
        break
#Задача 2
while (True):
    quastion = int(input("Введіть цифру від 1 до 12: "))
    if (quastion == 1):
        print("Січень")
        break
    elif (quastion == 2):
        print("Лютий")
        break
    elif (quastion == 3):
        print("Березень")
        break
    elif (quastion == 4):
        print("Квітень")
        break   
    elif (quastion == 5):
        print("Травень")
        break
    elif (quastion == 6):
        print("Червень")
        break
    elif (quastion == 7):
        print("Липень")
        break
    elif (quastion == 8):
        print("Серпень")
        break
    elif (quastion == 9):
        print("Вересень")
        break
    elif (quastion == 10):
        print("Жовтень")
        break
    elif (quastion == 11):
        print("Листопад")
        break
    elif (quastion == 12):
        print("Грудень")
        break
#Задача 3
while (True):
    quastion = int(input("Введіть число: "))
    if (quastion > 0):
        print("Number is positive")    
        break
    elif (quastion < 0 ):
        print("Number is negative")
        break
    elif (quastion == 0):
        print("Number is equal to zero")
        break
#Задача 4
a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
if (a == b):
    print("Числа рівні")
else:
    print("Числа не рівні")
    if (a > b):
        print(b)
        print(a)
    else:
        print(a)
        print(b)    