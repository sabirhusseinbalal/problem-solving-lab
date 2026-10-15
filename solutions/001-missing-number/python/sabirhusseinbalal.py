# Puzzle #001 — Missing Number

numbers = [1, 2, 3, 4, 6, 7, 8, 9, 10]


def find_missing_number(numbers):
    # Check every expected number from 1 to 10.
    for number in range(1, 11):
        if number not in numbers:
            return number

    # No missing number was found.
    return None


print(find_missing_number(numbers))  # 5
print(find_missing_number([1, 2, 4, 5, 6, 7, 8, 9, 10]))  # 3
