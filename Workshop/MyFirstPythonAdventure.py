door_greetings = {'1': "Welcome to the paradise!", '2': "Welcome the next dimension" }



print()

print("What is your name?")
name = input(">  ")


print(f"Hello {name}! ")
print("Welcome to the dungeon!")
print("Do you go through door 1 or door 2?")

door = input("> ")

print(door_greetings[door])

if door == "1":
    print("There is a nice vampire asking you if you enjoy life.")
    print("What do you do?")
    print("1. Smile and nod")
    print("2. Scream and run")

    vampire = input("> ")

    if vampire == "1":
        print(f"Congratulations {name}, you found a new friend!")
    elif vampire == "2":
        print(f"Sorry {name}, the vampire is faster. You become a dinner.")
    else:
        print("Your are not so good with numbers, are you?")

elif door == "2":
    print("It is dark and you hear a scaring sound...")
    print("What you do?")
    print("1. You ask who is there?")
    print("2. You run away?")

    scared = input("> ")

    if scared == "1":
        print("you are really courageous!")
    elif scared == "2":
        print("Maybe you should start to learn some Kung-fu...")
    else:
        print("Maybe you first need a coffee before trying again...")

else:
    print("You maybe are hallucinating, we only have 2 doors...")

