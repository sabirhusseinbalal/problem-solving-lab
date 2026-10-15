# Puzzle #005 — Zero Shifter

numbers = [0, 3, 0, 1, 4, 0, 5]


def move_zeros(numbers):
    result = []
    zero_count = 0

    # Keep non-zero numbers in their original order.
    for number in numbers:
        if number == 0:
            zero_count += 1
        else:
            result.append(number)

    # Add the zeros to the end.
    for _ in range(zero_count):
        result.append(0)

    return result


print(move_zeros(numbers))  # [3, 1, 4, 5, 0, 0, 0]
print(numbers)  # Original list is unchanged.
