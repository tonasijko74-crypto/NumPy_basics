import numpy as np

# all zeros matrix
print(np.zeros(5))
print(np.zeros((2, 3)))
print(" ")

# all ones matrix
print(np.ones(5))
print(np.ones((2, 3)))
print(" ")

# any other number
print(np.full((2, 2), 5))
print(" ")

# full_like if you want the same shape as an existing array

# random decimal numbers
print(np.random.randn(2, 3))

# random integer values
print(np.random.randint(2, size=(3, 3)))

# the identity matrix
print(np.identity(3))
print(" ")

# task from video
print("task from video")
x=np.ones((5, 5))
x[1:4, 1:4]=0
x[2, 2]=9
print(x)

print(" ")
# array copy - be careful!!!
f=np.array([1, 2, 3])
b=f.copy()
b[0]=100
print(b)
print(f)