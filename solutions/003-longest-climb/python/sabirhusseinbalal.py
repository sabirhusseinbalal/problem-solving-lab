# Puzzle #003 — Longest Climb

numbers = [1, 2, 4, 3, 5, 6, 7, 2]


def longest_increasing_streak(numbers):
    if not numbers:
        return 0

    # A single number starts a streak of length 1.
    streak = 1
    longest = 1

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            streak += 1
        else:
            streak = 1

        if streak > longest:
            longest = streak

    return longest


print(longest_increasing_streak(numbers))  # 4
print(longest_increasing_streak([3, 5, 4, 6, 7]))  # 3
print(longest_increasing_streak([]))  # 0
