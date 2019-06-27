import pandas as pd
from sys import argv


def pheno_corr(data, theraptrix_ps):
    data = pd.read_csv(data, sep='\t', index_col=0)
    with open(theraptrix_ps) as f:
        thera_proteins = [line.strip() for line in f.readlines()]
    data = data[(data['Exp Sig'] == True) & (data['Protein'].isin(thera_proteins))]
    grouped_means = data.groupby('Cell Type').mean()
    print(grouped_means)
    pheno_data = grouped_means.iloc[:,-7:] #3 when on test data
    print(pheno_data)
    max_value = pheno_data.max().max()
    cell_type = pheno_data.max(axis=1).idxmax()
    pheno = pheno_data.max(axis=0).idxmax()
    outfile = 'results/4.txt'
    with open(outfile, 'w') as outfile:
        outfile.write('{:.3f}'.format(round(max_value, 3))+'\n')
        outfile.write(f'{(cell_type, pheno)}')

if __name__ == '__main__':
    pheno_corr(argv[1], argv[2])

# pheno_corr('locus_data.tab', 'theraptrix_protein_orders.txt')
