from sys import argv
from collections import defaultdict
from operator import itemgetter

def parse_bed(infile):
    chr_map = defaultdict(list)
    with open(infile) as infile:
        for i, line in enumerate(infile):
            line = line.strip().split()
            chromo, start, stop, *_, strand = line
            if strand == '+':
                size = int(stop) - int(start)
                chr_map[chromo].append({'len':size, 'idx': i})

    for ls in chr_map.values():
        ls.sort(key=itemgetter('len'))
    top5 = [ls[-5:] for ls in chr_map.values()]
    total = sum(sum(d['idx'] for d in ls) for ls in top5)
    with open('results/3.txt', 'w') as result:
        result.write(str(total))

if __name__ == "__main__":
    parse_bed(argv[1])
