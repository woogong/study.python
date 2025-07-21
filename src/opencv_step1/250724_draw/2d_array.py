import numpy as np

array = np.array([[2, 4, 6, 8], [3, 6, 9, 12]])
print(array)
print(array.shape)
print(array[0, 1]) # I think it prints 4 -> good

print('*' * 32)

for idx_row, row in enumerate(array):
    for idx_column, value in enumerate(row):
        print(f"{idx_row}, {idx_column} : {value}")