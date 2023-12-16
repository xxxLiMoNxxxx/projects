"""#1 Завдання
print("\n 1 Завдання \n")

def sum(a, b):
    return a + b
def minus(a, b):
    return a - b
def dil(a, b):
    return a / b
def ymn(a, b):
    return a * b

while(True):
    while (True):
        a = int(input("Введіть перше число: "))
        b = int(input("Введіть друге число: "))
        quastion = int(input("Що ви хочете? \n 1 - сума, 2 - мінус, 3 - ділення, 4 - добуток "))
        if (quastion == 1):
            print("Вийшло:", sum(a, b))
            print("\n ------------------------------------------------------------------ \n")
            break
        elif (quastion == 2):
            print("Вийшло:", minus(a, b))
            print("\n ------------------------------------------------------------------ \n")
            break
        elif (quastion == 3):
            print("Вийшло:", dil(a, b))
            print("\n ------------------------------------------------------------------ \n")
            break
        elif (quastion == 4):
            print("Вийшло:", ymn(a, b))
            print("\n ------------------------------------------------------------------ \n")
            break
        else:
            print("Помилка, ви не те написали")
            print("\n ------------------------------------------------------------------ \n")
            break"""
#2 Завдання 
print("\n 2 Завдання \n")
pib = input("Введіть свій ПІБ: ")
group = input("Введіть свою группу: ")
age = input("Введіть свій вік: ")
blood = input("Введіть свою група крові: ")

students_dict = {pib : {"Группа":group,
                        "Вік":age,
                        "Группа крові": blood},}
print(students_dict)