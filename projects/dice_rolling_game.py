import random

 
while True:
    choice = input('roll the dice? enter (y/n): ').lower()

    if choice =='y':
        dia1=random.randint(1,6)
        dia2=random.randint(1,6)

        print(f'({dia1},{dia2})')
    elif choice=='n':
        print('thanks for playing')
        break
    else:
        print('invalid choice')