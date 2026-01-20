# Task 1: Blast off!

# Ask for inputs
end_number = int(input("Enter a number to count up to: "))
step = int(input("Enter a step amount: "))

# Use a for loop to count up
for number in range(0, end_number + 1, step):
    print(number)

# Print the final message
print("Blast off!")
