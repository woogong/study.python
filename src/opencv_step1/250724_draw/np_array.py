import numpy as np

array1 = np.array([1, 2, 3, 4, 5])
print(f"type : {type(array1)}")
print(f"ndim : {array1.ndim}")
print(f"shape : {array1.shape}")
print(f"dtype : {array1.dtype}")

print("-" * 50)

array2 = np.array([[1, 2, 3], [4, 5, 6]])
print(f"type : {type(array2)}")
print(f"ndim : {array2.ndim}")
print(f"shape : {array2.shape}")
print(f"dtype : {array2.dtype}")

print("-" * 50)

array3 = np.array([1, 2, 3], ndmin=3)
print(f"value : {array3}")
print(f"type : {type(array3)}")
print(f"ndim : {array3.ndim}")
print(f"shape : {array3.shape}")
print(f"dtype : {array3.dtype}")
