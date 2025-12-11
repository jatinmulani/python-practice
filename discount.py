price = float(input('enter your price'))

if (price > 1000):
    print(price*0.10)
elif (price < 1000 and price > 500):
    print(price*0.05)
else:
    print('no discount')
