import matplotlib.pyplot as plt
import numpy as np

arr = [
        [1,2,3],
        [4,5,6]
    ]
print(arr)

n_arr = np.array(arr)

print(arr[0][1])
print(n_arr[0,1])
print(n_arr.tolist())