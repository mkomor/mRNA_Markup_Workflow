import sys

f=open(sys.argv[1],'w')
f.write('mRNAmarkup Report\n\n')

#fasta file with input sequences
f1=open(sys.argv[2])
lines=f1.readlines()
f1.close()

n=0
for i in lines:
	if '>' in i:
		n=n+1

f.write('\n\t Number of input sequences: \t\t\t\t\t'+str(n))

#fasta file with blast hits (UniVec)
f1=open(sys.argv[3])
lines=f1.readlines()
f1.close()

n=0
for i in lines:
	if '>' in i:
		n=n+1

f.write('\n\t Number of potential vector-contaminated sequences: \t\t'+str(n))

#fasta file with blast hits (BacterialDB)
f1=open(sys.argv[4])
lines=f1.readlines()
f1.close()

n=0
for i in lines:
	if '>' in i:
		n=n+1

f.write('\n\t  Number of potential bacterial-contaminated sequences: \t'+str(n))

#fasta file with blast hits (ReferenceDB)
f1=open(sys.argv[5])
lines=f1.readlines()
f1.close()

n=0
for i in lines:
	if '>' in i:
		n=n+1

f.write('\n\t  Number of sequences matching the ReferenceDB: \t\t'+str(n))


#Full length
f1=open(sys.argv[6])
lines=f1.readlines()
f1.close()

n=0
for i in lines:
	if '>' in i:
		n=n+1

f.write('\n\t\t  Number of potential full-length coding sequences: \t'+str(n))



#Non-qual
f1=open(sys.argv[7])
lines=f1.readlines()
f1.close()

n=0
for i in lines:
	if '>' in i:
		n=n+1

f.write('\n\t\t  Non-qualifying sequences: \t\t\t\t'+str(n))

#chim
f1=open(sys.argv[8])
lines=f1.readlines()
f1.close()

n=0
for i in lines:
	if '>' in i:
		n=n+1

f.write('\n\t\t\t  Number of potential chimeric sequences: \t'+str(n))

#Non-qual seq
f1=open(sys.argv[9])
lines=f1.readlines()
f1.close()

n=0
for i in lines:
	if '>' in i:
		n=n+1

f.write('\n\t\t\t  Non-qualifying sequences: \t\t\t'+str(n))

#AllProt
f1=open(sys.argv[10])
lines=f1.readlines()
f1.close()

n=0
for i in lines:
	if '>' in i:
		n=n+1

f.write('\n\t  Number of sequences matching the AllProteinDB: \t\t'+str(n))


#ProtdomDB
f1=open(sys.argv[11])
lines=f1.readlines()
f1.close()

n=0
for i in lines:
	if '>' in i:
		n=n+1

f.write('\n\t  Number of sequences matching the ProteinDomainDB: \t\t'+str(n))



#remain
f1=open(sys.argv[12])
lines=f1.readlines()
f1.close()

n=0
for i in lines:
	if '>' in i:
		n=n+1

f.write('\n\t  Number of remaining sequences: \t\t\t\t'+str(n))





