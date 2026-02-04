print("Welcome to the quiz!!!")

playing = input("Would you like to play? ")

if playing.lower() != "yes":
    quit("Maybe next time!")

print("Awesome! Let's play a game!!!")
score = 0


answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ").lower()
if answer == "random processing unit":
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What does SSD stand for? ").lower()
if answer == "solid state drive":
    print("Correct!")
else:
    print("Incorrect!")

print("you got " + str(score) + " questiosn correct!")
