# Ticket Price Calculator

# Ask for age
age = int(input("Enter your age: "))

# Ask if they are a student
student = input("Are you a student? (Yes/No): ")

# Determine base ticket price
if age < 12:
    price = 8
elif age <= 17:
    price = 10
elif age <= 64:
    price = 12
else:
    price = 6

# Apply discount if applicable
if student == "Yes" and age > 12:
    price = price - 2

# Display final price
print("Your ticket price is: $", price)




# Ticket Price Calculator

# Ask for age
age = int(input("Enter your age: "))

# Ask if they are a student
student = input("Are you a student? (Yes/No): ").strip().lower()

# Determine base ticket price
if age < 12:
    price = 8
elif 12 <= age <= 17:
    price = 10
elif 18 <= age <= 64:
    price = 12
else:
    price = 6

# Apply discount if applicable
if student == "yes" and age > 12:
    price -= 2

# Display final price
print(f"Your ticket price is: ${price:.2f}")
