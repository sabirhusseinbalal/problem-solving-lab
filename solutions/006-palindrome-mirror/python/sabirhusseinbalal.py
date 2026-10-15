# Puzzle #006 — Palindrome Mirror


def is_palindrome(text):
    text = text.lower()

    # Compare characters from opposite ends.
    for i in range(len(text) // 2):
        if text[i] != text[len(text) - 1 - i]:
            return False

    return True


print(is_palindrome("CIVIC"))  # True
print(is_palindrome("python"))  # False
print(is_palindrome(""))  # True
