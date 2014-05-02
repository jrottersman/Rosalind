f = open("c:/scripts/rosalind/rosalind_dna.txt", "r")
list_dna = list(f.read())
f.close
a = 0
c = 0 
g = 0
t = 0
for i in xrange(len(list_dna)):
	if list_dna[i] == 'A': a +=1
	elif list_dna[i] == 'C': c += 1
	elif list_dna[i] == 'G': g += 1
	elif list_dna[i] == 'T': t += 1

print ("A is equal to %s C is equal to %s G is equal to %s and T is equal to %s ") % (a, c, g, t)