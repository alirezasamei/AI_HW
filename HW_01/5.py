import random

floor = 1
seiling = 100
rand = random.randint(floor,seiling)
print(f"true value is: {rand}")
while True:
    guess = float(input(f"enter your guessed number (suggested number : {int((floor + seiling)/2)}): "))
    if(guess > rand):
        print("large")
        seiling = guess
    elif(guess < rand):
        print("low")
        floor = guess
    else:
        break
print("congratulations. You reached the desired number.")
