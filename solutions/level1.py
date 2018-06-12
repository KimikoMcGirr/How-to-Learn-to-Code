# -*- coding: utf-8 -*-
"""
My answer to the problem for level 1.
"""

from sys import argv
from scipy.stats import ttest_ind

def calc_mutation_rates(infasta, ref_seq):
    """Finds difference for each seqence in fasta file, given a reference sequence"""
    with open(infasta) as infasta:
        infasta = infasta.readlines()
    sequences = [line.strip() for line in infasta if line[0] != '>']

    distances = []
    for seq in sequences:
        dist = sum(1 for n1, n2 in zip(seq, ref_seq) if n1 != n2)
        distances.append(dist)
    return distances

def mutation_significance(ref, control, thera):
    """Writes p-value of t-test between control and thera files for mutation rates."""
    with open(ref) as ref:
        ref = ref.readlines()
    ref_seq = ref[1].strip()

    control_counts = calc_mutation_rates(control, ref_seq)
    test_counts = calc_mutation_rates(thera, ref_seq)
    pval = ttest_ind(control_counts, test_counts)[1]

    with open('results/1.txt', 'w') as outfile:
        outfile.write(str(round(pval, 4)))

if __name__ == '__main__':
    mutation_significance(argv[1], argv[2], argv[3])
