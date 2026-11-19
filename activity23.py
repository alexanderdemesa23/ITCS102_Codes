route = ["bayan","sm","dll"]
pasahero = []
SEATS = 6
FARE = 13
TOTAL = 0

while True:
    print()
    print("sakay:", pasahero)
    print(len(pasahero), "of", SEATS, "seats")
    print("1 sakay 2 priority seat 3 para po!")
    print("4 baba sa pinto 5 baba sa harap")
    print("6 seat check 7 balikan 8 exit")
    choice = input("Choice: ")

    if choice == "1":
        if len(pasahero) == SEATS:
            print("puno na!")
        else:
            name = input("Name: ")
            pasahero.append(name)
            TOTAL = TOTAL + FARE
            print(name, "dun ka sa likod.")

    elif choice == "2":
        if len(pasahero) == SEATS:
            print("puno na")
        else:
            name = input("Name: ")
            pasahero.insert(0, name)
            TOTAL = TOTAL + FARE
            print(name, "took the priority seat!")

    elif choice == "3":
        name = input("sino baba na? ")
        if name in pasahero:
            pasahero.remove(name)
            print(name, "get off. ingat! ")
        else:
            print(name, "is not on this jeep")

    elif choice == "4":
        if len(pasahero) == 0:
            print("the jeep is empty")
        else:
            left = pasahero.pop()
            print(left, "got off the door")

    elif choice == "5":
        if len(pasahero) == 0:
            print("the jeep is empty")
        else:
            front = pasahero.pop(0)
            print(front, "got off the front")

    elif choice == "6":
        for i in range(len(pasahero)):
            print("Seat", i + 1, pasahero[i])

    elif choice == "7":
        route.reverse()
        print("Route:", route)

    elif choice == "8":
        print("Total fare today:" , TOTAL)
        break
    else:
        print("invalid choice. ")
