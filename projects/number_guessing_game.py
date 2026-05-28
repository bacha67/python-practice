import random

secret_number=random.randint(1,100)
try:
 guess = int(input('enter your guess: '))
except ValueError:
   print('pleas enter a valid number')

while guess!=secret_number:

 if guess > secret_number:
    print("Too high")
 elif guess < secret_number:
     print("Too low")
 guess = int(input("Try again: "))

print('correct!')
