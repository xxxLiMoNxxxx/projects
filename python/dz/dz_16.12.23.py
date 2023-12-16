"""#1 Завдання
print("\n 1 Завдання \n")
pib = input("Введіть свій ПІБ: ")
group = input("Введіть свою группу: ")
age = input("Введіть свій вік: ")
blood = input("Введіть свою група крові: ")

students_dict = {pib : {"Группа":group,
                        "Вік":age,
                        "Группа крові": blood},}
print(students_dict)"""
#2 Завдання
print("\n 2 Завдання \n")
all_contacts = []

for i in range(1, 11+1):
    name = input("Введіть ім`я контакта: ")
    number = input("Введіть номер контакта: ")
    contacts_dict = { f"Контакт {i}": {"Ім`я контакта": name,
                                          "Номер контакта":number},}
    all_contacts.append(contacts_dict)
    while(True):
        quastion = int(input("Що далі? \n 1 - додати новий контакт, 2 - подивитися всі контакти "))
        if (quastion == 1):
            if(i == 10):
                print("У вас вже максимально контактів")
            elif(i < 10):
                break
        elif (quastion == 2):
            if(i == 10):
                print(all_contacts)
            elif(i < 10):
                print(all_contacts)
                break
    