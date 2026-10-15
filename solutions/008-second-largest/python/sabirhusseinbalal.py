# Puzzle #008 — Second-Largest Number

numbers = [4, 8, 2, 8, 6, 4]


def second_largest(numbers):
    largest = None
    second = None

    for number in numbers:
        if largest is None or number > largest:
            second = largest
            largest = number
        elif number != largest:
            if second is None or number > second:
                second = number

    return second


print(second_largest(numbers))  # 6
print(second_largest([5]))  # None
print(second_largest([5, 5, 5]))  # None
