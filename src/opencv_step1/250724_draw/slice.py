import numpy as np

list = []
for i in range(0, 100):
    list.append(i)

array = np.array(list)
print(array)

even = array[::2]
print(even)

odd = array[1::2]
print(odd)

multiple3 = array[::3]
print(multiple3)

negative = array[-10:]
print(negative)

print('-' * 32)


row = []

for i in range(0, 10):
    column = []
    for j in range (0, 10):
        column.append(i + j)
    row.append(column)
    
array2d = np.array(row)
print(array2d)

slice1 = array2d[0:2]
print(slice1)

slice2 = array2d[0:2, 6]
print(slice2)

slice3 = array2d[9, 5:]
print(slice3)