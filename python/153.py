try:
    numbers = list(map(
        int,
        input("Enter numbers separated by spaces: ").split()
    ))

    total = 0

    for number in numbers:
        total += number

    print("Sum of numbers:", total)

except ValueError:
    print("Please enter integers only.")