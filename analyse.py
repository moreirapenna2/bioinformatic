"""
from Bio import SeqIO
from Bio.Alphabet import IUPAC
from Bio.SeqUtils import GC
from Bio import Geo


for seq_record in SeqIO.parse("sequence.gbk", "genbank"):
    print(seq_record.id)
    #print(repr(seq_record.seq))
    print(len(seq_record))


myseq = seq_record.seq
print(myseq)

print(myseq[0])
print(len(myseq))

porcg = (100 * float(myseq.count("G"))/ len(myseq))
porcc = (100 * float(myseq.count("C"))/ len(myseq))
porct = (100 * float(myseq.count("T"))/ len(myseq))
porca = (100 * float(myseq.count("A"))/ len(myseq))
gctotal = GC(myseq)


print("G%:  "+str(porcg))
print("C%:  "+str(porcc))
print("T%:  "+str(porct))
print("A%:  "+str(porca))
print("GC total:  "+str(gctotal))

print("Complement: "+str(myseq.complement()))
print("Reversed: "+str(myseq[::-1]))
"""
import GEOparse
import pandas as pd


gse = GEOparse.get_GEO(filepath="GDS5606_full.soft.gz")

#print(gse.columns)
#print("\n\n\n")
#print(gse.database.metadata)

gse.show_table()
print("\n\n")
print(gse._get_columns_as_string())

db = pd.DataFrame()
