# Puzzle #007 — Pair Finder

numbers = [7, 1, 5, 3, 6, 4]
target = 6


def find_pair(numbers, target):
    # Pick one item, then check every item after it.
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return (numbers[i], numbers[j])

    return None


print(find_pair(numbers, target))  # (1, 5)
print(find_pair([2, 4, 7], 9))  # (2, 7)
print(find_pair([3, 4], 6))  # None
