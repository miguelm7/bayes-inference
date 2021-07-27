import sys
import random
from readcsv import *


print(v2_probs_tt)
class PriorSampling:
	CPTs={} #dictionary

	def __init__(self, netID):
		self.initialiseNet(netID)		

	def initialiseNet(self, netID):
		#print(v1_probs)
		#print(v1_probs_f)
		
		if netID == "luca":
			self.CPTs["P"]={"+p":v1_probs[0], "-p":v1_probs_f[0]} #peerpresssure
			self.CPTs["A"]={"+a":v1_probs[1], "-a":v1_probs_f[1]} #anxiety  #keys = {values} 
			
			self.CPTs["S"]={"+s|+a+p":v3_probs_ttt[0], "-s|+a+p":v3_probs_ftt[0], #smoking|anxiety,pp
					"+s|-a+p":v3_probs_tft[0], "-s|-a+p":v3_probs_fft[0],
					"+s|+a-p":v3_probs_ttf[0], "-s|+a-p":v3_probs_ftf[0],
					"+s|-a-p":v3_probs_tff[0], "-s|-a-p":v3_probs_fff[0]}
			self.CPTs["Y"]={"+y|+s":v2_probs_tt[0], "-y|+s":v2_probs_ft[0], 
					"+y|-s":v2_probs_tf[0], "-y|-s":v2_probs_ff[0]}
			self.CPTs["G"]={"+g":v1_probs[2], "-g":v1_probs_f[2]}
			self.CPTs["LC"]={"+lc|+s+g":v3_probs_ttt[1], "-lc|+s+g":v3_probs_ftt[1], 
					"+lc|-s+g":v3_probs_tft[1], "-lc|-s+g":v3_probs_fft[1],
					"+lc|+s-g":v3_probs_ttf[1], "-lc|+s-g":v3_probs_ftf[1],
					"+lc|-s-g":v3_probs_tff[1], "-lc|-s-g":v3_probs_fff[1]}
			self.CPTs["AD"]={"+ad|+g":v2_probs_tt[1], "-ad|+g":v2_probs_tt[1], 
					"+ad|-g":v2_probs_tf[1], "-ad|-g":v2_probs_ff[1]}
			self.CPTs["ED"]={"+ed":v1_probs[3], "-ed":v1_probs_f[3]}
			self.CPTs["All"]={"+all":v1_probs[4], "-all":v1_probs_f[4]}
			self.CPTs["C"]={"+c|+all+lc":v3_probs_ttt[2], "-c|+all+lc":v3_probs_ftt[2], 
					"+c|+all-lc":v3_probs_tft[2], "-c|+all-lc":v3_probs_fft[2],
					"+c|-all+lc":v3_probs_ttf[2], "-c|-all+lc":v3_probs_ftf[2],
					"+c|-all-lc":v3_probs_tff[2], "-c|-all-lc":v3_probs_fff[2]}
			self.CPTs["F"]={"+f|+lc+c":v3_probs_ttt[3], "-f|+lc+c":v3_probs_ftt[3], 
					"+f|+lc-c":v3_probs_tft[3], "-f|+lc-c":v3_probs_fft[3],
					"+f|-lc+c":v3_probs_ttf[3], "-f|-lc+c":v3_probs_ftf[3],
					"+f|-lc-c":v3_probs_tff[3], "-f|-lc-c":v3_probs_fff[3]}
			self.CPTs["CA"]={"+ca|+ad+f":v3_probs_ttt[4], "-ca|+ad+f":v3_probs_ftt[4], 
					 "+ca|+ad-f":v3_probs_tft[4], "-ca|+ad-f":v3_probs_fft[4],
					 "+ca|-ad+f":v3_probs_ttf[4], "-ca|-ad+f":v3_probs_ftf[4],
					 "+ca|-ad-f":v3_probs_tff[4], "-ca|-ad-f":v3_probs_fff[4]}
			self.CPTs["order"]=["P","A", "S", "Y", "G", "LC", "AD", "ED", "All", "C", "F","CA"]
			self.CPTs["parents"]={"P":None,"A":None,  "S":"A,P", "Y":"S","G":None, "LC":"S,G","AD":"G","ED":None,"All":None,"C":"All,LC","F":"LC,C","CA":"AD,F"}		
			

		else:
			print("UNKNOWN network="+str(netID))
			exit(0)

	def sampleVariable(self, CPT, conditional):
		sampledValue=None
		randnumber=random.random()

		value1=CPT["+"+conditional]
		value2=CPT["-"+conditional]

		if randnumber<=value1:
			sampledValue="+"+conditional
		else:
			sampledValue="-"+conditional

		return sampledValue.split("|")[0]

	def sampleVariables(self, printEvent):
		event=[]
		sampledVars={}

		for variable in self.CPTs["order"]:
			evidence=""
			conditional=""
			parents=self.CPTs["parents"][variable]
			if parents==None:
				conditional=variable.lower()
			else:
				for parent in parents.split(","):
					evidence+=sampledVars[parent]
				conditional=variable.lower()+"|"+evidence

			sampledValue=self.sampleVariable(self.CPTs[variable], conditional)
			event.append(sampledValue)
			sampledVars[variable]=sampledValue
				
		if printEvent: print(event)
		return event

if __name__ == "__main__":
	ps=PriorSampling("luca")
	ps.sampleVariables(True)# this method will give you an event
