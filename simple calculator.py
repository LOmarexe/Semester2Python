def calculator():
    # Input the expression
    expression = input("Enter your calculation: ")

    # Evaluate the expression and print the result
    result = eval(expression)
    print(f'The result is: {result}')


calculator()


answer = input("Want to calculate something again? (Y/N): ")

while answer == 'Y':
    calculator()
    answer = input("Want to calculate something again? (Y/N): ")

print('Have a good day!')
