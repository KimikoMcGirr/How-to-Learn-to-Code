"""
Solution
--------

My answer to the problem for level 2.

@author: sksuzuki
"""
## Level 2
import sys
import pathlib
import os
import numpy as np

def temperature(folder):
    '''
    The main function that finds the max value of a cell and finds
    that cell's index.

    Note: There are two ways to retrieve all of the data from different
    subfolders using the functions 'get_data_with_os' and 'get_data_with_pathlib'.

    Arguements
    ----------
    folder - str: path to wt_folder

    '''
    count, data = get_data_with_os(folder)
    # count, data = get_data_with_pathlib(folder)
    data /= count
    hottest = int(round(data.max()))
    idx = np.unravel_index(np.argmax(data), data.shape)
    print(str(idx), file=open("results/2.txt", "w"))
    print(str(hottest), file=open("results/2.txt", "a"))

def get_data_with_os(folder):
    data = None
    count = 0
    for subf in os.walk(folder):
        # print(subf)
        if subf[2]:
            for file in subf[2]:
                if file.endswith(".csv"):
                    new_data = np.loadtxt(subf[0]+"/"+file,delimiter=',')
                    new_data[new_data==0] = 76
                    if data is None:
                        data = new_data
                    else:
                        data += new_data
                    count += 1
    return count, data

def get_data_with_pathlib(folder):
    data = None
    for count, csv in enumerate(pathlib.Path(folder).glob('**/*.csv'), start=1):
        new_data = np.loadtxt(csv, delimiter=',')
        new_data[new_data == 0] = 76
        if data is None:
            data = new_data
        else:
            data += new_data
    return count, data

if __name__ == "__main__":
    temperature(sys.argv[1])

# Testing
# print(temperature("C:/Users/sksuzuki/Documents/CodeStories/EXCISION/level_2/level2_data"))
