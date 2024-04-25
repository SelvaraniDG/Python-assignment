def remove_duplicates(list):
    seen = set()
    res = []
    for item in list:
        if item not in seen:
            res.append(item)
            seen.add(item)
    return res

user_input = input("Enter the list of numbers separated by spaces: ")
list = [int(x) for x in user_input.split()]

result = remove_duplicates(list)
print("List after removing duplicates:", result)