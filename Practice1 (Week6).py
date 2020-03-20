# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 11:25:19 2020

@author: 10139
"""

# 1. GC content calculator
DNA = input()
base = 0
for n in DNA:
    if n == 'C' or n == 'G':
        base += 1
content = base/len(DNA)*100
print ('The GC content for the specified DNA is', content, '%.')

#2. Complementary DNA strand calculator
DNA_reverse = DNA[:]
DNA_reverse = DNA_reverse[::-1] #reverse the string
cDNA = ''
for n in DNA_reverse:
    if n == 'A':
        cDNA = cDNA + 'T'
    elif n == 'T':
        cDNA = cDNA + 'A'
    elif n == 'C':
        cDNA = cDNA + 'G'
    elif n == 'G':
        cDNA = cDNA + 'C'
print ('The complementary DNA strand (from 5’ to 3’) is', cDNA, '.')
 
#3. DNA to mRNA convertor
cDNA_reverse = cDNA[:]
cDNA_reverse = cDNA_reverse[::-1] 
mRNA = ''
for n in cDNA_reverse:
    if n == 'T':
        mRNA = mRNA + 'U'
    else:
        mRNA = mRNA + n
print ('The mRNA sequence is', mRNA, '.')

#4. mRNA to protein
proteins = {'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L', 'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L', 'AUU':'I', 'AUC':'I', 'AUA':'I', 'AUG':'M', 'GUU':'V', 
           'GUC':'V', 'GUA':'V', 'GUG':'V', 'UCU':'S', 'UCC':'S', 'UCA':'S', 'UCG':'S', 'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P', 'ACU':'T', 'ACC':'T',
           'ACA':'T', 'ACG':'T', 'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A', 'UAU':'Y', 'UAC':'Y', 'CAU':'H', 'CAC':'H', 'CAA':'K', 'CAG':'K', 'GAU':'D',
           'GAC':'D', 'GAA':'E', 'GAG':'E', 'UGU':'C', 'UGC':'C', 'UGG':'G', 'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGU':'S', 'AGC':'S', 'AGA':'R',
           'AGG':'R', 'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G'}
start = mRNA.find('AUG')
stop = 0
protein = ''
if start == -1:
    print ('The mRNA sequence does not contain any start codon.')
else:
    for n in range (start, len(mRNA)-2, 3):
        if mRNA[n:n+3] == 'UAA' or mRNA[n:n+3] == 'UGA' or mRNA[n:n+3] == 'UAG':
            stop = n
            break
    if stop == 0:
        print ('The mRNA sequence does not contain any stop codon.')
    else:
        for n in range (start, stop, 3):
            protein += proteins[mRNA[n:n+3]]
        print ('The polypeptide sequence from the mRNA sequence(', mRNA, ') is', protein, '.')

#5. Additional function
