def find_biggest(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

# Example usage:
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

biggest = find_biggest(number1, number2)
print("The biggest number is:", biggest)


