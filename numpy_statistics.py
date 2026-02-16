import numpy as np

stats=np.array([[1,2,3],[4,5,6]])
print(np.min(stats))
print(np.max(stats))

print(np.sum(stats))
print(" ")

# reorganizing arrays
before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)
print(" ")
after=before.reshape((2, 2, 2))
print(after)

# vertical stacking vector
v1=np.array([1,2,3,4])
v2=np.array([5,6,7,8])
print(np.vstack([v1,v2]))
print(" ")