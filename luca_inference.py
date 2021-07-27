import sys
import random

from sampling_parameters import PriorSampling 

count={}
#ps = PriorSampling("sprinkler")
ps = PriorSampling("luca")

#comentar
def RejectionSampling(X,e,N):

	index = getIndex(X)
	for j in range(1, N):
		
		x = ps.sampleVariables(False)
		if isConsistent(x,e):
			val=x[index]
			if val in count:
				count[val]+=1
			else:
				count[val]=1
	#print(count) 
	return count


		#comentar
def isConsistent(event,evidence):
	if evidence =='': return True

	for varvalue in evidence:
		if varvalue not in event:
			return False
	#print("se cumple")
	return True
#comentar
def getIndex(X):
	variables = ps.CPTs["order"]
	for i in range(0,len(variables)):
		if variables[i] == X:
			return i
#comentar
def normalize(x,y):
	aux = x+y
	alpha = 1.0/aux
	nx = x*alpha
	ny = y*alpha
	return nx,ny


if __name__ == "__main__":
	e ={"+c","+f"} #given coughing and fatigue
	X = "S" #smoking
	N=10000
	count = RejectionSampling(X,e,N)
	print(count)
	#cosa = str(ps.CPTs[X].keys())

	#comentar
	x=count.pop("+s")
	y=count.pop("-s")
	xnorm, ynorm = normalize(x,y)
	print("probability distribution: <" + str(xnorm) + "," + str(ynorm) + ">" )
	


	
		
	

