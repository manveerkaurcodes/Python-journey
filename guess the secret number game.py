secret=10
while True:
    guess=int(input("enter your guess"))
    if(guess<10):
        print("too low,try again")
    elif(guess>10):
        print("too high,try again")
    else:
        print("guess is correct,you win!!(:")
    break