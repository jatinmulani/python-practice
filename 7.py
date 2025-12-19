# n = int(input('enter from user'))
# for i in range(n, 0, -1):
#     for j in range(n-i):
#         print(' ', end=' ')
#     for k in range(1, i+1):
#         print(k, end=' ')
#     print()
balance = 5000
print("ATM ")
print("1. check balance")
print("2. deposit money")
print("3. withdraw money")
select_a_number = int(input("select a number "))
if (select_a_number == 1):
    print("your balance is ", balance)
elif (select_a_number == 2):
    amount = int(input('enter amount to deposit'))
    balance += amount
    print('deposited successfully')
    print('remianing balance', balance)
elif (select_a_number == 3):
    withdrwal = int(input('enter your amount'))
    balance -= withdrwal
    print('withdrawl successfully')
    print('remianing balance', balance)
else:
    print("enter a valid number")
