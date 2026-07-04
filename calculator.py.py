num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1/2/3/4): ")

if choice == "1":
    print("Answer =", num1 + num2)

elif choice == "2":
    print("Answer =", num1 - num2)

elif choice == "3":
    print("Answer =", num1 * num2)

elif choice == "4":
    if num2 != 0:
        print("Answer =", num1 / num2)
    else:
        print("Cannot divide by zero!")

else:
    print("Invalid choice!")