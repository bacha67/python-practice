unit = input('enter the unit you want to convert to c or f : ')
temp = input('enter the temprature  you want to convert:')
if unit =='c':
    print(f'{temp}F is {float(temp)-32*9/5}C')
elif unit ==f:
    print(f'{temp}C is {float(temp)*9/5+32}F')
else: 
    print('you enter invalid data')