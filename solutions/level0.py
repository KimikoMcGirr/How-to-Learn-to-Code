#!/usr/bin/env python

from sys import argv

def calc(seq):
    """Calculate GC content of sequence as a percent."""
    gc = seq.count('G')+seq.count('C')
    gc = round(gc/len(seq) * 100)
    with open('results/0.txt', 'w') as outfile:
        outfile.write(f'{gc}%')

if __name__ == '__main__':
    calc(argv[1])
