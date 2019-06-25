import pandas as pd
from sys import argv

def getLongestLines(filepath):
    data=pd.read_table(filepath,sep='\t',names=['Chromosome','start','end','name','score','strand'])
    data=data[data['strand']=='+']
    data['difference']=data['end']-data['start']
    diff=data.groupby('Chromosome').apply(lambda p:p['difference'].nlargest(5))
    lines=diff.index.values
    total=[y for x,y in lines]

    return sum(total)


if __name__=='__main__':
    filepath=argv[1]
    #filepath=r'C:\Users\jumpi\How-to-Learn-to-Code\data\3\ENCFF239FSU.bed'
    linetotal=getLongestLines(filepath)
    with open('results/3.txt','w') as file:
        file.write(str(linetotal))
