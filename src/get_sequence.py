# get_sequence.py

from Bio import Entrez

def fetch_record(genbank_id):
    Entrez.email = "your_email@email.com"
    handle = Entrez.efetch(db="nucleotide", id=genbank_id, \
                           rettype="gb", retmode="xml")
    records = Entrez.read(handle)
    return records

def get_sequence(records):
    return records[0]["GBSeq_sequence"]

genbank_id = "MN908947"
records = fetch_record(genbank_id)
sequence = get_sequence(records)

print(len(sequence))
print(sequence)

