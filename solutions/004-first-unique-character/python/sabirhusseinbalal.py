# Puzzle #004 — First Unique Character

text = "aabcddeeb"


def first_unique_character(text):
    for character in text:
        count = 0

        # Count this character using a simple loop.
        for other_character in text:
            if character == other_character:
                count += 1

        if count == 1:
            return character

    return None


print(first_unique_character(text))  # c
print(first_unique_character("aabb"))  # None
