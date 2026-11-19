def manual_reverse(items):
    if not items:
        return []
    
    reversed_list = []
    for i in range(len(items) - 1, -1, -1):
        reversed_list.append(items[i])
    return reversed_list
