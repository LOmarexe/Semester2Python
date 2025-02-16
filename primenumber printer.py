def Prime(n):
    prime = True  # Assume the number is prime
    for i in range(2, n):
        if n % i == 0:
            prime = False  # If divisible, it's not prime
            break  # Stop checking further
    if prime and n > 1:
        print(n)  # Print the prime number

def printPrimes():
    for num in range(2, 121):  # Loop from 2 to 120
        Prime(num)  # Check and print if it's prime

# Run the function
printPrimes()
