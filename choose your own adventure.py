name = input("Type your name: ")
print(f"Welcome {name} to this adventure")

answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ")

if answer == "left":
    answer = input(
        "you come to a river, you can walk around it or swim across. Type walk to walk around and swim to swim accross: ")

    if answer == "swim":
        print("You swam accross and you were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and lost the game.")
    else:
        print("Not a valid option. You lose. ")

elif answer == "right":
    answer = input(
        "You come to a bridge, it looks wobbly, do you want to corss it or head back (Cross/Back)")

    if answer == "back":
        print("You fell off a cliff and died.")
    elif answer == "cross":
        answer = input(
            "You cross the bridge and meet a stranger. Do you talk to them (yes/no)")

        if answer == "yes":
            print(
                "You talk to them. They give you gold. Congratulations you have won the game!!!")

        elif answer == "no":
            print("You ignor the stranger and they are offended. You lost.")

        else:
            print("Not a valid option. You lose. ")

    else:
        print("Not a valid option. You lose. ")
else:
    print("Not a valid option. You lose :(")

print(f"Thank you for trying {name}")
