while (True):
    coast = 0
    money = int(input("Введіть скільки у вас грошей: "))
    pirishki = int(input("Чи ви хочите пиріжечок? Він коштуе 50 грн: 1/2 \n 1 - так, 2 - пропустити "))
    if (pirishki == 1):
        if (coast + 50 > money):
            print("Вам не хватае.")
        elif (coast+50 < money):
            coast+=50
            burger = int(input("Чи ви хочите бургер? Він коштуе 150 грн: 1/2 \n 1 - так, 2 - пропустити ")) 
            if (burger == 1):
                if (coast+150 > money):
                    print("Вам не хватае.")
                elif (coast+150 < money):
                    coast+=150
                    cola = int(input("Чи ви хочите колу? Вона коштуе 35 грн: 1/2 \n 1 - так, 2 - пропустити "))  
                    if (cola == 1):
                        if (coast+35 > money):
                            print("Вам не хватае, це було останне в меню, ви скупились на:", coast)
                        elif (coast+35 < money):
                            coast+=35
                            print("Це було останне в меню, ви скупились на:", coast)
                    elif (cola == 2):
                        if (coast > 0):
                            print("Це було останне в меню, ви скупились на:", coast)
                        elif (coast == 0):
                            print("Ви нічого не купили")
            elif (burger == 2):
                cola = int(input("Чи ви хочите колу? Вона коштуе 35 грн: 1/2 \n 1 - так, 2 - пропустити "))      
                if (cola == 1):
                    if (coast+35 > money):
                        print("Вам не хватае, це було останне в меню, ви скупились на:", coast)
                    elif (coast+35 < money):
                        coast+=35
                        print("Це було останне в меню, ви скупились на:", coast)
                elif (cola == 2):
                    if (coast > 0):
                        print("Це було останне в меню, ви скупились на:", coast)
                    elif (coast == 0):
                        print("Ви нічого не купили")  
    elif (pirishki == 2):
        burger = int(input("Чи ви хочите бургер? Він коштуе 150 грн: 1/2 \n 1 - так, 2 - пропустити ")) 
        if (burger == 1):
            if (coast+150 > money):
                print("Вам не хватае.")
            elif (coast+150 < money):
                coast+=150
                cola = int(input("Чи ви хочите колу? Вона коштуе 35 грн: 1/2 \n 1 - так, 2 - пропустити "))  
                if (cola == 1):
                    if (coast+35 > money):
                        print("Вам не хватае, це було останне в меню, ви скупились на:", coast)
                    elif (coast+35 < money):
                        coast+=35
                        print("Це було останне в меню, ви скупились на:", coast)
                elif (cola == 2):
                    if (coast > 0):
                        print("Це було останне в меню, ви скупились на:", coast)
                    elif (coast == 0):
                        print("Ви нічого не купили")
        elif (burger == 2):
            cola = int(input("Чи ви хочите колу? Вона коштуе 35 грн: 1/2 \n 1 - так, 2 - пропустити "))      
            if (cola == 1):
                if (coast+35 > money):
                    print("Вам не хватае, це було останне в меню, ви скупились на:", coast)
                elif (coast+35 < money):
                    coast+=35
                    print("Це було останне в меню, ви скупились на:", coast)
            elif (cola == 2):
                if (coast > 0):
                    print("Це було останне в меню, ви скупились на:", coast)
                elif (coast == 0):
                    print("Ви нічого не купили")