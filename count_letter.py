def count_letter(sentence, target):
    if len(target) != 1:
        return "Constraint Error: Target must be a single letter."
    
    count = 0
    for char in sentence.lower():
        if char == target.lower():
            count += 1
    return count
