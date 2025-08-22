#Write a Python function to find the factorial of a number.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))  # Output: 120
print(factorial(0))  # Output: 1
