import numpy as np

def square(x):
    """Square a number"""
    return x ** 2

def volume_converter(volume, unit):
    """Convert certain SI volumes to mLs"""
    conversions = {'mL': 1E-3, 'uL': 1E-6, 'nL': 1E-9, 'kL': 1E3}
    return round(volume * conversions[unit], 10)

def squared_sum(in_list):
    """Finds the sum of squares of a list of numbers."""
    return np.sum(np.array(in_list)**2)
