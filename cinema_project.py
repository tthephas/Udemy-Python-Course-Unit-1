# project that checks to see if person is old enough to see a certain film

films = {
    "Finding Dory": [3, 5],
    "Bourne": [18, 5],
    "Tarzan": [15, 1],
    "Ghost Busters": [12, 5],
}

while True:
    choice = input("What film would you like to see today?: ").strip().title()

    if choice in films:
        # check user age
        age = int(input("How old are you?: ").strip())

        if age >= films[choice][0]:
            # check if there are seats
            if films[choice][1] > 0:
                print("Enjoy the film!")
                films[choice][1] = films[choice][1] - 1
            else:
                print("Sorry we are sold out!")
        else:
            print("You are too young to see this film sorry.")

    else:
        print("We arent showing that film sorry.")
