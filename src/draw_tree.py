from Bio import Phylo

tree = Phylo.read("covid.all.ph","newick")
Phylo.draw(tree)

