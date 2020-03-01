# run_muscle.py

from Bio.Align.Applications import MuscleCommandline

muscle_exe = "/절대경로/muscle3.8.31_i86darwin64"

cmd_line = MuscleCommandline(muscle_exe, \
                             input="covid.all.fasta", \
                             out="covid.all.aln", \
                            clw=" ")

print(cmd_line)
stdout, stderr = cmd_line()

