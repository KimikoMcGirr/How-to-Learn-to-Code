import pandas as pd
from sys import argv

def parse_bed(bed):
    df = pd.read_csv(bed, sep='\t', header=None)
    df.columns = ['chromosome', 'start', 'stop', 'ID', 'score', 'strand']
    df_p = df[df['strand'] == '+'].copy()
    df_p['len'] = df_p['stop'] - df['start']
    chromo_names = df_p['chromosome'].unique()

    df_top = []
    for contig in chromo_names:
        df_contig = df_p[df_p['chromosome'] == contig]
        df_top.append(df_contig.nlargest(5,'len'))
    df_top = pd.concat(df_top)

    with open('results/3.txt', 'w') as result:
        result.write(str(sum(df_top.index)))

if __name__ == "__main__":
    parse_bed(argv[1])
    # parse_bed('../data/3/ENCFF239FSU.bed')
