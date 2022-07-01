from twolinks import *
import random,math

def a(n): #objective function
	if(n== [0 for i in range(len(n))]):
		return 0
	# #Independent
	# return -sum([(i+1-n[i])**2 for i in range(len(n))])

	perchannel = 1000/sum(n)
	return sum([(i+1)*n[i]*perchannel for i in range(len(n))])

def noise(): #generate noise. values from [-1,0,1].
	p = 0.2
	seed = random.random()
	if(seed<p):
		return -1
	if(seed>1-p):
		return 1
	return 0
#Vector Operations:
def mult(a,b): #adding two vectors
	return [a[i]*b[i] for i in range(len(a))]
def add(a,b): #adding two vectors
	return [a[i]+b[i] for i in range(len(a))]
def sub(a,b): #subtracting two vectors
	return [a[i]-b[i] for i in range(len(a))]
def scale(l,v):
	return [l*x for x in v]
def mag(n):
	return math.sqrt(sum([x**2 for x in n]))
#Real to Int casting
def realToInt(x): #mapping reals to ints probabilistically.
	if(x>=1):
		return 1
	elif(x>=0):
		# return round(x)
		if(random.random()<x):
			return 1
		else:
			return 0
	else: #x<0
		return -realToInt(-x)

def realToIntVector(n,scale): #mapping vector of reals to vector of ints
	return [realToInt(scale*x) for x in n]

def zeroes(k):
	return [0 for i in range(k)]

def castback(n):
	return [min(max(x,10), 50) for x in n]

def simulate(alpha,k):
	random.seed(1220)
	iterations = 100

	nprev = zeroes(k)
	ncur = [1 for i in range(k)]
	total = zeroes(k)
	m = zeroes(k)
	regret = 0
	for t in range(iterations):
		if(ncur!=nprev):
			rate = 0.1*(a(ncur) - a(nprev))
			step = scale(rate, sub(ncur, nprev))

			m = add(scale(alpha,m), scale(1-alpha,step))
			ncur,nprev = castback(add(ncur,realToIntVector(m,1))),ncur
		else:
			ncur,nprev = [min(max(10,x+noise()),50) for x in ncur],ncur

		total = add(total,ncur)
		regret += a(ncur)
		print(ncur)
	print("average choice:")
	print(scale(1/iterations,total))
	print('avg regret:')
	print(regret/iterations)
	print(iterations)
	return (regret/iterations)

def searchOptimal(k):
	maxim = float('-inf')
	search = 20
	for i in range(search):
		print(i/search)
		val = simulate(i/search,k)
		if(val>maxim):
			maxim = val
			maxalpha = i/search
	return maxalpha

	print("optimal: " + str(maxalpha))
def main():
	# maxk = 20
	# vals = [0 for i in range(maxk)]
	# for k in range(1,maxk):
	# 	vals[k] = searchOptimal(k)
	# print(vals)
	# print(sum(vals)/len(vals))

	simulate(0.1,10)

if __name__ == "__main__":
	main()
#[0, 0.95, 0.95, 0.7, 0.4, 0.9, 0.55, 0.4, 0.85, 0.7, 0.75, 0.55, 0.35, 0.4, 0.05, 0.3, 0.15, 0.65, 0.6, 0.8]
