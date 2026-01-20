numbers = [1, 2, 3, 4]

with open("numbers.txt", "w") as file:
    for num in numbers:
        file.write(str(num) + "\n")
