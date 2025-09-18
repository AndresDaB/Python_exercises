def remove_duplicate(s):
    result = []
    seen = set()

    for char in s:
        if char not in seen:
            result.append(char)
            seen.add(char)
    
    return ''.join(result)

s = 'mississippi'
print(remove_duplicate(s))
