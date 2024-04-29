import numpy as np

array_3d = np.zeros((3, 5, 8))
array_str = np.array_str(array_3d).replace('.', ',')

print(array_str)