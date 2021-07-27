import csv

'''
## probability IDs
row[0] #smoking
row[1] #Yellow f
row[2] #Anxiety
row[3] #Peerpressure
row[4] #genetics
row[5] #attention disorder
row[6] #born evenday
row[7] #car accident
row[8] #fatigue
row[9] #allergy
row[10] #coughing
row[11] #lung cancer
'''


vector1 = [3,2,4,6,9]  #declare a vector with the identifiers for each variable
v1_names = ['P(PP)','P(A)','P(G)','P(ED)','P(All)']
v1_probs =[0.0,0.0,0.0,0.0,0.0] #declare vectors to store the probability values
v1_probs_f =[0.0,0.0,0.0,0.0,0.0]
v1_names_f = ['P(¬PP)','P(¬A)','P(¬G)','P(¬ED)','P(¬All)']
cont1 = [0,0,0,0,0] #declare 


vector2 = [1,5] #declare a vector with the identifiers for each variable
vector2_var = [0,4]  #declare a vector with the identifiers for evidence variables
v2_names_tt = ['P(Y|S)','P(AD|G)']
v2_names_ft = ['P(¬Y|S)','P(¬AD|G)']
v2_names_tf = ['P(Y|¬S)','P(AD|¬G)']
v2_names_ff = ['P(¬Y|¬S)','P(¬AD|¬G)']
v2_probs_tt =[0.0,0.0] #declare vectors to store the probability values
v2_probs_ft =[0.0,0.0]
v2_probs_tf =[0.0,0.0]
v2_probs_ff =[0.0,0.0]
cont2tt = [0,0]
cont2ft = [0,0]
cont2tf = [0,0]
cont2ff = [0,0]
cont2_vart = [0,0]
cont2_varf = [0,0]

vector3 = [0,11,10,8,7]   #declare a vector with the identifiers for each variable
vector3_var1 = [2,0,9,11,5] #declare a vector with the identifiers for first evidence variables
vector3_var2 = [3,4,11,10,8] #declare a vector with the identifiers for second evidence variables
v3_names_ttt = ['P(S|A,PP)','P(LC|S,G)','P(C|All,LC)','P(F|LC,C)','P(CA|AD,F)']
v3_names_tft = ['P(S|¬A,PP)','P(LC|¬S,G)','P(C|¬All,LC)','P(F|¬LC,C)','P(CA|¬AD,F)']
v3_names_ttf = ['P(S|A,¬PP)','P(LC|S,¬G)','P(C|All,¬LC)','P(F|LC,¬C)','P(CA|AD,¬F)']
v3_names_tff = ['P(S|¬A,¬PP)','P(LC|¬S,¬G)','P(C|¬All,¬LC)','P(F|¬LC,¬C)','P(CA|¬AD,¬F)']
v3_names_ftt = ['P(¬S|A,PP)','P(¬LC|S,G)','P(¬C|All,LC)','P(¬F|LC,C)','P(¬CA|AD,F)']
v3_names_fft = ['P(¬S|¬A,PP)','P(¬LC|¬S,G)','P(¬C|¬All,LC)','P(¬F|¬LC,C)','P(¬CA|¬AD,F)']
v3_names_ftf = ['P(¬S|A,¬PP)','P(¬LC|S,¬G)','P(¬C|All,¬LC)','P(¬F|LC,¬C)','P(¬CA|AD,¬F)']
v3_names_fff = ['P(¬S|¬A,¬PP)','P(`LC|¬S,¬G)','P(¬C|¬All,¬LC)','P(¬F|¬LC,¬C)','P(¬CA|¬AD,¬F)']
v3_probs_ttt =[0.0,0.0,0.0,0.0,0.0] #declare vectors to store the probability values
v3_probs_tft =[0.0,0.0,0.0,0.0,0.0]
v3_probs_ttf =[0.0,0.0,0.0,0.0,0.0]
v3_probs_tff =[0.0,0.0,0.0,0.0,0.0]
v3_probs_ftt =[0.0,0.0,0.0,0.0,0.0]
v3_probs_fft =[0.0,0.0,0.0,0.0,0.0]
v3_probs_ftf =[0.0,0.0,0.0,0.0,0.0]
v3_probs_fff =[0.0,0.0,0.0,0.0,0.0]

cont3ttt =[0,0,0,0,0]
cont3tft =[0,0,0,0,0]
cont3ttf =[0,0,0,0,0]
cont3tff =[0,0,0,0,0]
cont3ftt =[0,0,0,0,0]
cont3fft =[0,0,0,0,0]
cont3ftf =[0,0,0,0,0]
cont3fff =[0,0,0,0,0]

cont3_varstt =[0,0,0,0,0]
cont3_varsft =[0,0,0,0,0]
cont3_varstf =[0,0,0,0,0]
cont3_varsff =[0,0,0,0,0]


with open('Data/lucas0_train.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
         line_count += 1

         for i in range(0,len(vector1)):
	       #count for 1
               if row[vector1[i]] == '1':
        	        cont1[i] = cont1[i] + 1
         for i in range(0,len(vector2)):
               #count for 2
               if row[vector2[i]] == '1' and row[vector2_var[i]] == '1':
        	       cont2tt[i] = cont2tt[i] + 1
               if row[vector2[i]] == '0' and row[vector2_var[i]] == '1':
        	       cont2ft[i] = cont2ft[i] + 1
               if row[vector2[i]] == '1' and row[vector2_var[i]] == '0':
        	       cont2tf[i] = cont2tf[i] + 1
               if row[vector2[i]] == '0' and row[vector2_var[i]] == '0':
        	       cont2ff[i] = cont2ff[i] + 1
               if row[vector2_var[i]] == '1':
        	        cont2_vart[i] = cont2_vart[i] + 1
               if row[vector2_var[i]] == '0':
        	        cont2_varf[i] = cont2_varf[i] + 1
         for i in range(0,len(vector3)):
               #count for 3
               if row[vector3[i]] == '1' and row[vector3_var1[i]] == '1' and row[vector3_var2[i]] == '1':
        	        cont3ttt[i] = cont3ttt[i] + 1
               if row[vector3[i]] == '1' and row[vector3_var1[i]] == '0' and row[vector3_var2[i]] == '1':
        	        cont3tft[i] = cont3tft[i] + 1
               if row[vector3[i]] == '1' and row[vector3_var1[i]] == '1' and row[vector3_var2[i]] == '0':
        	        cont3ttf[i] = cont3ttf[i] + 1
               if row[vector3[i]] == '1' and row[vector3_var1[i]] == '0' and row[vector3_var2[i]] == '0':
        	        cont3tff[i] = cont3tff[i] + 1
               if row[vector3[i]] == '0' and row[vector3_var1[i]] == '1' and row[vector3_var2[i]] == '1':
        	        cont3ftt[i] = cont3ftt[i] + 1
               if row[vector3[i]] == '0' and row[vector3_var1[i]] == '0' and row[vector3_var2[i]] == '1':
        	        cont3fft[i] = cont3fft[i] + 1
               if row[vector3[i]] == '0' and row[vector3_var1[i]] == '1' and row[vector3_var2[i]] == '0':
        	        cont3ftf[i] = cont3ftf[i] + 1
               if row[vector3[i]] == '0' and row[vector3_var1[i]] == '0' and row[vector3_var2[i]] == '0':
        	        cont3fff[i] = cont3fff[i] + 1

               if row[vector3_var1[i]] == '1' and row[vector3_var2[i]] == '1':
        	       cont3_varstt[i] = cont3_varstt[i] + 1
               if row[vector3_var1[i]] == '0' and row[vector3_var2[i]] == '1':
        	       cont3_varsft[i] = cont3_varsft[i] + 1
               if row[vector3_var1[i]] == '1' and row[vector3_var2[i]] == '0':
        	       cont3_varstf[i] = cont3_varstf[i] + 1
               if row[vector3_var1[i]] == '0' and row[vector3_var2[i]] == '0':
        	       cont3_varsff[i] = cont3_varsff[i] + 1
        

for i in range(0,len(vector1)):
        v1_probs[i] =  (cont1[i] + 1)/(line_count + 2)
        print(v1_names[i] + ' = ' + str(v1_probs[i]))
        v1_probs_f[i] = 1 - v1_probs[i]
        print(v1_names_f[i] + ' = ' + str(v1_probs_f[i]))

for i in range(0,len(vector2)):
        v2_probs_tt[i] =  (cont2tt[i] + 1)/(cont2_vart[i] + 2)
        print(v2_names_tt[i] + ' = ' + str(v2_probs_tt[i]))
        v2_probs_ft[i] = (cont2ft[i] + 1)/(cont2_vart[i] + 2)
        print(v2_names_ft[i] + ' = ' + str(v2_probs_ft[i]))
        v2_probs_tf[i] =  (cont2tf[i] + 1)/(cont2_varf[i] + 2)
        print(v2_names_tf[i] + ' = ' + str(v2_probs_tf[i]))
        v2_probs_ff[i] = (cont2ff[i] + 1)/(cont2_varf[i] + 2)
        print(v2_names_ff[i] + ' = ' + str(v2_probs_ff[i]))

for i in range(0,len(vector3)):
        v3_probs_ttt[i] =  (cont3ttt[i] + 1)/(cont3_varstt[i] + 2)
        print(v3_names_ttt[i] + ' = ' + str(v3_probs_ttt[i]))
        v3_probs_tft[i] =  (cont3tft[i] + 1)/(cont3_varsft[i] + 2)
        print(v3_names_tft[i] + ' = ' + str(v3_probs_tft[i]))
        v3_probs_ttf[i] =  (cont3ttf[i] + 1)/(cont3_varstf[i] + 2)
        print(v3_names_ttf[i] + ' = ' + str(v3_probs_ttf[i]))
        v3_probs_tff[i] =  (cont3tff[i] + 1)/(cont3_varsff[i] + 2)
        print(v3_names_tff[i] + ' = ' + str(v3_probs_tff[i]))
        v3_probs_ftt[i] =  (cont3ftt[i] + 1)/(cont3_varstt[i] + 2)
        print(v3_names_ftt[i] + ' = ' + str(v3_probs_ftt[i]))
        v3_probs_fft[i] =  (cont3fft[i] + 1)/(cont3_varsft[i] + 2)
        print(v3_names_fft[i] + ' = ' + str(v3_probs_fft[i]))
        v3_probs_ftf[i] =  (cont3ftf[i] + 1)/(cont3_varstf[i] + 2)
        print(v3_names_ftf[i] + ' = ' + str(v3_probs_ftf[i]))
        v3_probs_fff[i] =  (cont3fff[i] + 1)/(cont3_varsff[i] + 2)
        print(v3_names_fff[i] + ' = ' + str(v3_probs_fff[i]))
        


print('Processed ' + str(line_count) + ' lines.')


