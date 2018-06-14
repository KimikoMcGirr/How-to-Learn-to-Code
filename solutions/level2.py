"""
Solution
--------

My answer to the problem for level 2.

@author: sksuzuki
"""
## Level 2
import sys
import pathlib
import numpy as np

def temperature(folder):
    data = None
    for i, csv in enumerate(pathlib.Path(folder).glob('**/*.csv'), start=1):
        new_data = np.loadtxt(csv, delimiter=',')
        new_data[new_data == 0] = 76
        if data is None:
            data = new_data
        else:
            data += new_data
    data /= i
    hottest = int(round(data.max()))
    idx = np.unravel_index(np.argmax(data), data.shape)
    with open("results/2.txt", "w") as f:
        f.write(f'{idx}\n')
        f.write(f'{hottest}')

if __name__ == "__main__":
    temperature(sys.argv[1])

# Testing purposes
# print(temperature("C:/Users/sksuzuki/Documents/EXCISION/level_2/data/"))
