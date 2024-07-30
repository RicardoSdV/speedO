from itertools import islice

import numpy as np

# Example with a Python list
python_list = [1, 2, 3, 4]
idx = 2
print(python_list[:idx])  # Output: [1, 2]

# Example with a NumPy array
np_array = np.array([1, 2, 3, 4])
idx = 2
print(np_array[:idx])  # Output: [1 2 3]

for el in islice(np_array, 2):
    print(el)

for el in islice(python_list, 2):
    print(el)