def get_consonant_value(c):
    return ord(c) - ord('a') + 1

def highest_consonant_value(s):
    vowels = "aeiou"
    max_value = 0
    current_value = 0

    for char in s:
        if char in vowels:
            max_value = max(max_value, current_value)
            current_value = 0
        else:
            current_value += get_consonant_value(char)

    return max(max_value, current_value)
