print("***Welcome to Quiz Game***\n\n")

playing = input("Do you want to play? ")
if playing.lower() != "yes": 
    exit()

name = input("\nEnter your name: ")
print(f"\nOkay! Let's play {name}:)")

score = 0

answer = input("\n\n(1) What does ALU stand for? ")
if answer.lower() == "arithmetic logic unit":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")

answer = input("\n\n(2) What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")

answer = input("\n\n(3) How many buttons a computer mouse has? ")
if answer.lower() == "two" or answer == "2":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")

answer = input("\n\n(4) First page of Website is termed as? ")
if answer.lower() == "homepage":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")

answer = input("\n\n(5) In which year, the Microsoft company was founded? ")
if answer == "1975":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")

answer = input("\n\n(6) What does BIOS stands for? ")
if answer.lower() == "basic input output system":
    print("Correct!")
    score = score + 1
else:
    print("Incorrect!")

if score == 6:
    print("\nGreat!!")
elif score ==5:
    print("\nWell done!")
elif score ==4:
    print("\nNice!")
elif score ==3:
    print("\nGood!")
elif score ==2:
    print("\nYou need to work more!")
elif score ==1:
    print("\nPoor!")
elif score ==0:
    print("\nVery poor!")

print(f"\n{name} answered '{score}' question(s) out of '6'")



