import numpy as np
data = list(map(int, input("Enter numbers: ").split()))

arr = np.array(data)

print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Max:", np.max(arr))
print("Min:", np.min(arr))