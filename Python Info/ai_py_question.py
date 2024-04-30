data = {
    'item1': {'name': 'Apple',
              'price': 1.50,
              'units': 20
              },
    'item2': {'name': 'Orange',
              'price': 1.50,
              'units': 23
              },
    'item3': {'name': 'Apple',
              'price': 1.50,
              'units': 20
              },
    'item4': {'name': 'Apple',
              'price': 1.50,
              'units': 20
              },  
}

total_cost = 0
total_units = 0

for item in data:
    price = data[item]['price']
    units = data[item]['units']
    total_cost += price * units
    total_units += units
average_price = total_cost / total_units
print(average_price)