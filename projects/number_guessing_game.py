import random

secret_number=random.randint(1,100)
while True:
    try:
        guess = int(input("Enter your guess: "))
        break
    except ValueError:
        print("Please enter a valid number")

while guess!=secret_number:

 if guess > secret_number:
    print("Too high")
 elif guess < secret_number:
     print("Too low")
 guess = int(input("Try again: "))

print('correct!')
