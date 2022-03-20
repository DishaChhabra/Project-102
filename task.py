print('')
print('This program will help in solving basic maths equations.')
print('')
print('Enter a number as per the list, for wahtever function you need.')
print('     1. Addition')
print('     2. Subtraction')
print('     3. Multiplication')
print('     4. Division')
print('')
choice = int(input('Enter a number: '))
print('')
print('Enter any two numbers for the chosen function.')
no1 = int(input('Enter the first number: '))
no2 = int(input('Enter the second number: '))
print('')

def add():
    print('The sum is -',no1+no2)

def subtract():
    print('The difference is -',no1-no2)

def multiply():
    print('The product is -',no1*no2)

def divide():
    print('The quotient is -',no1/no2,'. The remainder is',no1%no2)

if choice==1:
    add()
elif choice==2:
    subtract()
elif choice==3:
    multiply()
elif choice==4:
    divide()
