#author MKomor
import sys

f=open(sys.argv[1])
lines=f.readlines()

f1=open(sys.argv[4],'w')
f2=open(sys.argv[3],'w')



ifintable=False
list1=[]
list2=[]
hits=[]
ifchimera=False

#if MuSeqBox with -M
for i in lines:
	if '!Potential chimera++:' in i:
		ifchimera=True
		break

#finding scores
if ifchimera==True:
	for i in lines:
		if 'chimera' in i:
			i1=i.split('Query ')
			i2=i1[1].split(' matches')
			hits.append(i2[0])
else:
	for i in lines:
		linia=i.split()
		if linia!=[]:
			if ifintable==True:
				if '----' in i:
					break
				if 'no_hit' not in linia:
					hits.append(linia[0])
			else:
				if '----' in i:
					ifintable=True

f.close()
f=open(sys.argv[2])
lines=f.readlines()
lines.append('>')

#writing to files
for i in range(len(lines)):

	if '>' in lines[i] and len(lines[i])>1:
		m=' '+lines[i]
		i1=m.split('|')
		i2=i1[1].split(' ')

		if i2[0] in hits:

			k=i+1
			f2.write(lines[i])
			while '>' not in lines[k]:
				f2.write(lines[k])
				k=k+1
		else:
			k=i+1
			f1.write(lines[i])
			while '>' not in lines[k]:
				f1.write(lines[k])
				k=k+1

		
		


