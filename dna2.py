#T he aim here is to write a function, so that when given to DNA strand sequences
# to output whether they are complimentary to each other.

# Some background knowledge on DNA; DNA is made of two strands which join and twist
# around each other forming a 'helix' shape. The way they join are using the bases 
# of the strands. There are four bases with simplified names A,T,C,G and A joins
# with T, C with G. 

# E.g ACGTGACAGT joins with TGCACTGTCA

# Also apparently sequences can be given in two different directions and basically 
# we need to reverse one of the strings. 



def check_dna(seq1,seq2):
	# First, convert seq1 from a string to a list.
	L1 = list(seq1)
	# Now convert seq2 to a list and reverse its order, so that they both run in the correct direction
	L2 = list(seq2)[::-1]
	# Name the smaller list S1 and the larger list S2
	if len(L1) < len(L2):
		S1 = list(seq1)
		S2 = list(seq2)[::-1]
	else:
		S2 = list(seq1)
		S1 = list(seq2)[::-1]
	# Convert the larger string into its compliment sequence i.e replacing C with G, G with C, A with T, T with A
	for n,i in enumerate(S2):
		if i == 'G':
			S2[n] = 'C'

		elif i == 'C':
			S2[n] = 'G'

		elif i == 'A':
			S2[n] = 'T'

		elif i == 'T':
			S2[n] = 'A'
	Indexes = []
	Assume = False
	# Find the indexes within S2 which the item of the list at this index is eqal to the first entry of S1 and that
	# have enough room left for the entire S1 string to attach to it, if possible
	for n,i in enumerate(S2):
		if i == S1[0] and len(S2)-n >= len(S1):
			Indexes.append(n)
	print Indexes
	# New idea: make a dictionary with the indexes from the Index list as the keys and the entries can be the following (length of S1) items
	# Then if one entry matches S1 return True
	Dictionary = {}
	for n in Indexes:
		Dictionary[n] = []
	for n in Indexes:
		for m,j in enumerate(S1):
			Dictionary[n].append(S2[n+m])
	for i in Dictionary:
		print Dictionary[i], S1
	for i in Dictionary:
		if Dictionary[i] == S1:
			return True
	else:
		return False





	

print check_dna('GCGCTGCTAGCTGATCGA','ACGTACGATCGATCAGCTAGCAGCGCTAC')