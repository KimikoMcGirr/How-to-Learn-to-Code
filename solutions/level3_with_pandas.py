import pandas as pd

def parse_bed(bed):
    df = pd.read_csv(bed, sep='\t', header=None)
    df_p = df[df[5] == '+'].copy()
    df_p[6] = df_p[2] - df[1]
    chromo_names = get_chromosome_names(df_p)

    df_top = []
    for contig in chromo_names:
        df_contig = df_p[df_p[0] == contig]
        df_top.append(df_contig.nlargest(5,6))
    df_top = pd.concat(df_top)

    with open('results/3.txt', 'w') as result:
        result.write(str(sum(df_top.index)))

def get_chromosome_names(df_p):
    return df_p[0].unique()

if __name__ == "__main__":
    bed = 'C:/Users/sksuzuki/Documents/EXCISION/level_3/ENCFF239FSU.bed'
    parse_bed(bed)
