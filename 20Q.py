guess_count = 20

print("20 Questions: \n ")

while guess_count != 0:
    c_one = input("Animal, Plant, Mineral?: ")
    guess_count -= 1
    print(guess_count)
    if c_one == "Animal" :
        c_two = input("Mammal, reptile, fish?: ")
        guess_count -= 1
        print(guess_count)
        if c_two == "Mammal":
            c_three = input("Bipedal, Quadruped: ")
            guess_count -= 1
            print(guess_count)
            if c_three == "Bipedal":
                print("You are thinking of a Human")
                print("Game Over")
                pass

            elif c_three == "Quadruped":
                c_four = input("Nocturnal, Diurnal: ")
                guess_count -= 1
                print(guess_count)
                if c_four == "Nocturnal":
                    c_five = input("Owl, Fox, Hedgehog")
        elif c_two == "reptile":
            c_three = input("Does it have legs?: Y/N: ")
            if c_three == "Y":
                c_four = input("Modern, Prehistoric: ")
                guess_count -= 1
                print(guess_count)
                if c_four == "Modern":
                    print("Lizard")
                if c_four == "Prehistoric":
                    print("Dinosaur")
            elif c_three == "N":
                c_four = input("Land, Sea: ")
                guess_count = 1
                print(guess_count)
                if c_four == "Land":
                    print("Snake")
                if c_four == "Sea":
                    print("Loch Ness Monster")
        elif c_two == "fish":
            c_three = input("Does it come with chips?: Y/N: ")
            guess_count -= 1
            print(guess_count)
            if c_three == "Y":
                c_four = input("Fillet, Rings, Nuggets: ")
                guess_count -= 1
                if c_four == "Fillet":
                    print("Haddock")
                if c_four == "Rings":
                    print("Kalamari")
                if c_four == "Nuggets":
                    print("Scampi")
            if c_three == "N":
                c_four = input("Is it oily? - Y/N: ")
                guess_count -= 1
                if c_four == "Y":
                    print("Mackerel")
                if c_four == "N":
                    print("Pollock")



    elif c_one == "Plant" :
        c_two = input("Vegetable, Fruit, Grass?: ")
        guess_count -= 1
        print(guess_count)
        if c_two == "Vegetable":
            c_three = input("Superterrainian, Subterrainian, Water: ")
            guess_count -= 1
            print(guess_count)
            if c_three == "Superterrainian":
                print("Peas")
            if c_three == "Subterrainian":
                print("Probably a potatoe")
            if c_three == "Water":
                print("Seaweed")
        if c_two == "Fruit":
            c_three = input("Berries, Nuts, Seeds: ")
            guess_count -= 1
            print(guess_count)
            if c_three == "Berries":
                print("Blackberries")
            if c_three == "Nuts":
                print("Walnuts")
            if c_three == "Seeds":
                print("Pumpkin seeds")
        if c_two == "Grass":
            c_three = input("West EU, Medditeranean, African: ")
            guess_count -= 1
            print(guess_count)
            if c_three == "West EU":
                print("Oats")
            if c_three == "Medditeranean":
                print("Bulgar Wheat")
            if c_three == "African":
                print("Maize")


    elif c_one == "Mineral" :
        c_two = input("Water soluble, Precious, Industrial?: ")
        guess_count -= 1
        print(guess_count)
        if c_two == "Water soluble":
            c_three = input("Superterrainian, Subterrainian, Water: ")
            guess_count -= 1
            print(guess_count)
            if c_three == "Superterrainian":
                print("Sulphur")
            if c_three == "Subterrainian":
                print("potassium")
            if c_three == "Water":
                print("Sodium")
        if c_two == "Precious":
            c_three = input("Jewels, Cars, Science: ")
            guess_count -= 1
            print(guess_count)
            if c_three == "Jewels":
                print("Gold")
            if c_three == "Cars":
                print("Neodymium/RAREEARTHS")
            if c_three == "Science":
                print("Magnesium")
        if c_two == "Industrial":
            c_three = input("Tagikizstan, Kazakstan, Uzbekistan: ")
            guess_count -= 1
            print(guess_count)
            if c_three == "Tagikizstan":
                print("inferior potassium")
            if c_three == "Kazakstan":
                print("Superior Potassium")
            if c_three == "Uzbekistan":
                print("Inferior potassium")


print("Out of guesses, Game Over")
play1 = input("Play Again? - Y/N: ")
