import math
def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
def square(n1):
    return n1**2
def cube(n1):
    return n1**3
def sqrt(n1):
    return math.sqrt(n1)

operations={
    '+':add,
    '-':subtract,
    '*':multiply,
    '/':divide,
    'square':square,
    'cube':cube,
    'sqrt':sqrt
}
def calculator():
    num1 = float(input('Enter the first number:'))
    while True:

        for symbol in operations:
            print(symbol)
        operation_symbol=input('Enter the operation:')
        if operation_symbol in ['+','-','*','/']:
            num2=float(input('Enter the next number:'))
            if operation_symbol=='/' and num2==0:
                print("Error:Cannot divide zero")
                continue
            operation_calculation=operations[operation_symbol]
            answer=operation_calculation(num1,num2)
            print(f'{num1} {operation_symbol} {num2} = {answer}')
        elif operation_symbol in ['square', 'cube', 'sqrt']:
            operation_calculation = operations[operation_symbol]
            answer = operation_calculation(num1)
            print(f'{operation_symbol} of {num1} = {answer}')

        else:
            print('Invalid operation Try Again')
            continue
        choice=input(f'Type y to continue calculating {answer},or\nType n for new calculation or q to quit:\n').lower()
        if choice=='y':
            num1=answer

        elif choice=='n':
            num1=float(input('Enter the first number:'))
        elif choice=='q':
            print('Quitting,Thanks for using')
            break

print('''
   ____      _            _       _             
  / ___|__ _| | ___ _   _| | __ _| |_ ___  _ __ 
 | |   / _` | |/ __| | | | |/ _` | __/ _ \| '__|
 | |__| (_| | | (__| |_| | | (_| | || (_) | |   
  \____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
''')
print('<----------Welcome To Calculator--------->')
calculator()