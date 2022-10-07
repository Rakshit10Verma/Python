import random
number=random.randint(0,50)
userinput=int(input("Enter your number\n"))
chances=0
while chances<5:
    if userinput==number:
        print("Congrats you won")
        break
    elif userinput<number:
        print("Your guess number is too low")
    else:
        print("Your guess is too high")
    chances+=1
    if not chances<5:
        print("You lose! The number is",number)
        break
    userinput=int(input("Enter your number"))
