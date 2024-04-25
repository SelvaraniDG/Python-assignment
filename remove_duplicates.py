def remove_duplicates(list):
    seen = set()
    res = []
    for item in list:
        if item not in seen:
            res.append(item)
            seen.add(item)
    return res

list = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]

result = remove_duplicates(list)
print(result)