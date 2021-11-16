#!/usr/local/bin/python3

# Exercise 1: processing DNA in a file. Write a programme that will trim the adapter and write the cleaned sequences to a new fille AND print the llength of eac adapter-free sequence to the screen. 

# Copy all the files needed to the repo Lect_12

# Do this part in Linux

cd LectureExercises/Lect_12
cp /localdisk/data/BPSM/Lecture12/* .

---- # Python3

import subprocess

input_txt_contents = open('input.txt').read()
input_txt_contents_vec = input_txt_contents.upper().split()

for seqs in input_txt_contents_vec :
    trimmed_seqs.write(seqs[14:] + '\n')
    seqs[14:]

trimmed_seqs = open('trimmed_seqs.txt', 'w')

trimmed_seqs.close()

# Check the output

subprocess.call("cat trimmed_seqs.txt",shell=True)

# Exercise 2: given the DNA sequence and the start/stop positions of exons (listen on separate lines and separated by commas), write a script that will extract exon segments, concatenate them and write them to a new file.

genomic_dna2 = open('genomic_dna2.txt').read().upper() #open and read genomic DNA as a string

# Read the exons file as a list - need to change the ',' to '\n', then split will put each new line into an element in the array

exons_v1 = open('exons.txt').read().replace(',','\n').split()

# Version 2:

exons_v3 = open('exons.txt').read().rsplit()
type(exons_v2)

with open('Exercise2_coding_seqence.fasta','w') as fullcoding :
    fullcoding.write('>Lecture12_exercise2_codingseq\n')
# Now extract the coding segments
counter = 0
for exons in exons_v3 :
    counter += 1
    startexon = int(exons.split(',')[0])-1
    endexon = int(exons.split(',')[1])
    exonwanted = genomic_dna2[startexon :endexon]
    fullcoding.write(exonwanted)
    regionsummary = 'Exon'+str(counter)+' '+str(exons)+' runs from index position '+str(startexon)+' upto but not including '+str(endexon)+ '.'
    print(regionsummary,'\n\t',exonwanted)

# Sliding windows 


