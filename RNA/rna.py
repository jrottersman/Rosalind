f = open("c:/scripts/rosalind/rosalind_rna.txt", "r")
list_dna = list(f.read())
f.close
r = open("c:/scripts/rosalind/rnatxt.txt", "w")
rna = ""
for i in xrange(len(list_dna)):
	if list_dna[i] == 'A': rna += 'A'
	elif list_dna[i] == 'C': rna += 'C'
	elif list_dna[i] == 'G': rna += 'G'
	elif list_dna[i] == 'T': rna += 'U'
rna_str = str(rna)
r.write(rna_str)
r.close