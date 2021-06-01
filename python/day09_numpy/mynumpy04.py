import numpy as np

arr = [
        [1,2,3],
        [4,5,6]
    ]

n_arr = np.array(arr)

r_arr = np.reshape(n_arr,(6,1))
l_arr = np.reshape(n_arr,(6))

#print(n_arr)
# print(r_arr)
