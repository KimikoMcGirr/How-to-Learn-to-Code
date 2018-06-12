# -*- coding: utf-8 -*-

import numpy as np

def make_lookup(names, seqs):
    """Create a dict using names as keys and seqs as values"""
    return dict(zip(names, seqs))

def headers(infasta):
    """Return the header names of a fasta formatted file"""
    return [line.strip('>') for line in infasta.split() if line[0]=='>']

def evens_mean(num_list):
    "Calculate the mean of all even elements in list"
    return np.mean([x for x in num_list if x%2==0])
