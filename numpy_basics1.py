import numpy as np

print("1 dimensional array") # 1d array
a=np.array([1,2,3])
print(a)
print(" ")

print("2 dimensional array") #2d array
b=np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])
print(b)
print(" ")

print("get dimension") # get dimension
c=a.ndim
d=b.ndim
print(c, d)
print(" ")

print("get shape") # get shape
a1=a.shape
b1=b.shape
print(a1, b1)
print(" ")

print("get type") # get type
z=a.dtype
print(z)
print(" ")

print("get size and total size")  # get size and total size
z=a.itemsize
print(z)
z=a.size
print(z)
print(" ")

print("access elements") # access
x=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(x[1, 5])

print("specific row and column ") # specific row
print(x[0, :])
print(x[:, 0])
print(x[0, 1:6:2])
x[1, 5]=20
print(x)
x[:, 2]=[1, 2]
print(x) 