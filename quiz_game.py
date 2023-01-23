print("Welcome to my nature quiz!")

playing = input("Do you want to play? ")

if playing.upper() != "YES":
    quit()

print("Okay! Lets PLAY!")
score = 0

answer = input("What is the color of the sky? ")
if answer.upper() == "BLUE":
    print("Correct!")
    score += 1
else:
    print("That is incorrect!")

answer = input("What is the color of grass? ")
if answer.upper() == "GREEN":
    print("Correct!")
    score += 1
else:
    print("That is incorrect!")

answer = input("What season is hot? ")
if answer.upper() == "SUMMER":
    print("Correct!")
    score += 1
else:
    print("That is incorrect!")


answer = input("What season is cold? ")
if answer.upper() == "WINTER":
    print("Correct!")
    score += 1
else:
    print("That is incorrect!")

print("You got " + str(score) +
      " questions correct! That's a score of " + str((score / 4) * 100) + "% ")
