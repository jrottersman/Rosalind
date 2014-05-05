f = open("c:/scripts/rosalind/rosalind_revc.txt", "r")
list_dna = list(f.read())
f.close
r = open("c:/scripts/rosalind/rnatxt2.txt", "w")
rev = ""
x = len(list_dna) 
for i in xrange(x):
	y = x - (i+1)
	if list_dna[y] == 'A': rev += 'T' 
	elif list_dna[y] == 'C': rev += 'G'
	elif list_dna[y] == 'G': rev += 'C'
	elif list_dna[y] == 'T': rev += 'A'
rev_str = str(rev)
r.write(rev_str)
r.close