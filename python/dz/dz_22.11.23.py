import datetime

#Задача 1
print("\n Задача 1 \n")
question = int(input("Введіть число: "))
for i in range(0, question+1, 2):
    print(i, end = " ")
#Задача 2
print("\n Задача 2 \n")
current_year = datetime.date.today().year
question = int(input("Введіть свій рік народження: "))
for i in range(0, current_year, 4):
    if (i > question):
        if (i%100 != 0 or i%1000 == 0):
            print(i, end=" ")
    