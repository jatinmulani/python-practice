num1 = float(input('enter your num'))
num2 = float(input('enter your num'))
operator = input("enter your operator (+,-,*,/):")
if (operator == '+'):
    print(num1+num2)
elif (operator == '-'):
    print(num1-num2)
elif (operator == '*'):
    print(num1*num2)
elif (operator == '/'):
    print(num1/num2)
else:
    print('input is zero')
