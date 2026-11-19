def count_vowels(text):
    if not isinstance(text, str):
        return 0
    
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
