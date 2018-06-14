## Level 2 Tasks
import os.path
import numpy as np

# Task 1
def rms(nums):
    """Return the root mean square of an array"""
    nums = np.asarray(nums)
    return np.sqrt(np.mean(nums**2))

    # Solution appending to a list using a for loop
    # ans = []
    # for x in nums:
    #     ans.append(x**2)
    # ans = sum(ans)/len(nums)
    # return ans**0.5

    # Solution appending to a list using a list comprehension
    # return (sum([x**2 for x in nums])/len(nums))**0.5

# Task 2
def parent_exists(file_path):
    """Tests if a file exists or returns it's parent directory"""
    if os.path.isfile(file_path):
        return "There is a file at that location."
    else:
        file_dir = os.path.dirname(file_path)
        return os.path.basename(file_dir)

# Testing fxn
# print(parent_exists('C:/Users/sksuzuki/Documents/GitHub/Excision/results/0.txt'))

# Task 3
def threshold(arr,limit):
    """Sets all alues in a numpy array below a limit to 0"""
    arr[arr < limit] = 0
    return arr

# Testing fxn
# print(threshold(np.array([[0,1,2],[0,4,4]]),3))
