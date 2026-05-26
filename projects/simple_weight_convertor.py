weight = float(input("Enter weight in pounds or Killogram: "))
unit = input('enter lbs or Kg: ')

if unit == 'Kg':
    print(f'weight: {weight*2.205}lbs pound')
elif unit == 'lbs':
    print(f'weight: {weight/2.205}Kg')
else:
    print('invalid unit')
