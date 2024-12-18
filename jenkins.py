# Sample Python Code

# A simple function to greet the user
def greet_user(name):
    print(f"Hello, {name}!")

# A function to calculate the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# A function to demonstrate a loop and conditional statements
def check_even_or_odd(number):
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

# Main block of the code
if __name__ == "__main__":
    # User input for greeting
    user_name = input("Enter your name: ")
    greet_user(user_name)

    # Factorial calculation
    num = int(input("Enter a number to calculate its factorial: "))
    print(f"The factorial of {num} is {factorial(num)}.")

    # Check if a number is even or odd
    number_to_check = int(input("Enter a number to check if it's even or odd: "))
    check_even_or_odd(number_to_check)
