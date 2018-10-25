import random
min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print("Tirando dado...")
    print("Sacaste....")
    print(random.randint(min, max))

    roll_again = input("¿Querés tirar el dado de nuevo?")