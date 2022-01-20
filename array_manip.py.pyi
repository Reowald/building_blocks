#https://stackoverflow.com/questions/15884527/how-can-i-prevent-the-typeerror-list-indices-must-be-integers-not-tuple-when-c

data = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1234, 12, 2)]

print(data[0])
print(data[0][0])
print(data[0][1])
print(data[0][2])

import numpy as np

new_array = np.empty()
