def print_contacts(all_contacts):
    for contact in all_contacts:
        for key, value in contact.items():
            print(f"{key}:")
            for sub_key, sub_value in value.items():
                print(f"  {sub_key}: {sub_value}")

all_contacts = []
contacts = []
i = 1

while(True):
    name = input("Введіть ім`я контакта: ")
    number = input("Введіть номер контакта: ")
    contacts_dict = { f"Контакт {i}": {"Ім`я контакта": name,
                                          "Номер контакта":number},}
    all_contacts.append(contacts_dict)
    i += 1
    while(True):
        quastion = input("Що далі? \n 1 - додати новий контакт, 2 - подивитися всі контакти \n 3 - видалити контакт")
        if (quastion == "1"):
            numbers_contacts = len(all_contacts)
            if(numbers_contacts == 9):
                print("\nУ вас вже максимально контактів\n")
                break
            else:
                break
        elif (quastion == "2"):
            print_contacts(all_contacts)
            break
        elif (quastion == "3"):
            print_contacts(all_contacts)
            delete = int(input("Який контакт хочете видалити? "))
            if(delete >= 1 and delete <= 10):
                all_contacts.pop(delete-1)
                for j in range(delete-1, len(all_contacts)):
                    all_contacts[j] = {f"Контакт {j+1}": all_contacts[j][f"Контакт {j+2}"]}
                i -= 1
                break
            else:
                print("Помилка, такого контакта нема")
                break
        else:
            print("\nПомилка, спробуйте ще раз\n")