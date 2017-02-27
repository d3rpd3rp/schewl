#!/usr/bin/python

#define sub routine to convert integers to binary in string form
def sub_divideby2(decnum):
	print decnum
	binstack = list()
	
	while decnum > 0:
		rem = decnum % 2
		binstack.append(rem)
		decnum = decnum // 2		
	
	return(binstack)

def sub_multby2(decnum,size):
	print decnum
	binstack = list()
	t=decnum
	#float(t)
	for i in range(1,size):
		t=t*2
		if t > 1:
			binstack.append(1)
			#t=t-1
		if t <= 0:
			binstack.append(0)
		print ('t is now {}'.format(t))
	print binstack

	return(binstack) 

print "This program will attempt to convert a decimal value to..."
print "...the IEEE-754 32bit Single Precision Floating Point Binary value." 
num = input("Enter any decimal value which will fit in a 32bit binary value: ")
num = str(num)
print num
#firstly, convert decimal to binary, noting the sign of the value
#also note if the value contains a decimal point
float=False
neg=False
if '.' in num:
	float=True
	print "Has dec. pt."
if '-' in num:
	neg=True
	print "Is negative."
#remove - sign
if neg is True:
	 num=num.replace(num[:1],'')
print ('string is now {}'.format(num))
#now let's do the most complex case, floating point
#use LHS and RHS to denote each side of the decimal point
if float is False:
	print "float is false"	
if float is True:
	sides=num.split(".",1)
	LHS=int(sides[0])
	RHS="0." + sides[1]
	print ('after split, RHS is {}'.format(RHS))
	RHS[::-1]
	print "RHS of type"
	print type(RHS)	
	binLHS=int(sub_divideby2(LHS))
	binLHS.reverse()
	binRHS=int(sub_multby2(RHS,(23-len(binLHS))))
	print('now the LHS is {}'.format(binLHS))
	print('now the RHS is {}'.format(binRHS))
#now determine the exponent radix is 2, so count how many points are on the LHS
	exp=len(str(LHS))
	binexp=sub_divideby2(exp)
	print('the de normalized binary string is')
	finalstring=list()
	if neg:
		finalstring.append(1)
	else:
		finalstring.append(0)
	finalstring.append(binexp)
	finalstring.append(binLHS)
	finalstring.append(binRHS)
	print finalstring
	  
