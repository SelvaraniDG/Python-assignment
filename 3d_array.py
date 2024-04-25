array = []

# for i in range(3):
#     layer = []
#     for j in range(5):
#         row = []
#         for k in range(8):
#             row.append(0)
#         layer.append(row)
#     array.append(layer)  

array = [[[0 for _ in range(8)] for _ in range(5)] for _ in range(3)]

for layer in array:
    for row in layer:
        print(row)
    print()              