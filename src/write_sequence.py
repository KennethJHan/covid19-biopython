from Bio import Entrez
from Bio import SeqIO
import pandas as pd

def fetch_record(genbank_id):
    Entrez.email = "your_email@email.com"
    handle = Entrez.efetch(db="nucleotide", id=genbank_id, \
                           rettype="gb", retmode="xml")
    records = Entrez.read(handle)
    return records

def write_sequence(genbank_id, records):
    print("## processing: "+genbank_id)
    record_id = records[0]["GBSeq_accession-version"]
    record_desc = records[0]["GBSeq_definition"]
    record_seq = records[0]["GBSeq_sequence"]
    with open(genbank_id+".fasta",'w') as fw:
        fw.write(">"+record_id+" "+record_desc+"\n")
        fw.write(record_seq+"\n")

def read_table(file):
    df = pd.read_csv(file, sep="\t")
    return df
        
file = "COVID-19.ncbi_list.200301.txt"
df = read_table(file)
complete_df = df[df["Gene Region"]=="complete"]
genbank_id_list = complete_df["GenBank"]

genbank_id_list = complete_df["GenBank"]
for genbank_id in genbank_id_list:
    records = fetch_record(genbank_id)
    write_sequence(genbank_id, records)

