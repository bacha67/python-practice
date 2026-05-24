items = input('enter the items you want to buy: ')
price = float(input('enter the price of the item: '))
quantity = int(input('enter the quantity of the item you want to buy: '))
total = price * quantity
print(f'you have bought {quantity}, {items}, {price}')
print(f'total cost: {total}')