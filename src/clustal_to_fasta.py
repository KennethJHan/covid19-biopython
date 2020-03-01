# clustal_to_fasta.py

with open("covid.all.aln",'r') as fr:
    for line in fr:
        if line.startswith("MUSCLE"):
            continue
        if "*" in line:
            continue
        l = line.strip().split()
        if l:
            genbank_id = l[0]
            seq = l[1]
            if genbank_id not in seq_dict:
                seq_dict[genbank_id] = seq
            else:
                seq_dict[genbank_id] += seq

with open("covid.aln.fasta",'w') as fw:
    for k,v in seq_dict.items():
        fw.write(">"+k+"\n")
        fw.write(v+"\n")

