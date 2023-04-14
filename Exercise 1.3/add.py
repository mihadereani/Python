a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operator = input("Enter operator (+ or -): ")

if operator == '+':
    result = a + b

elif operator == '-':
    result = a - b

else:
    print('Unknown operator')

print('Result: ', result)
