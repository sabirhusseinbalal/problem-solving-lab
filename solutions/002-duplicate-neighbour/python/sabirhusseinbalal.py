# Puzzle #002 — Duplicate Neighbour

numbers = [2, 5, 3, 3, 7, 7, 7, 9]


def find_duplicate_neighbour(numbers):
    # Compare each item with the item immediately before it.
    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i - 1]:
            return numbers[i]

    return None


print(find_duplicate_neighbour(numbers))  # 3
print(find_duplicate_neighbour([1, 2, 3, 4]))  # None
