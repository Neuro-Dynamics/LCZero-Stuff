# LCZero Brain Surgeon
# Alain Bellon (TheDreamMaster)
#
# Merges two LCZero nets of the same size
# Adjust interpolation values at your will

# Defaults for a 'Value Head' transplant:
# rInterp = 1.0
# pInterp = 1.0
# vInterp = 0.0

import sys
import numpy as np

residual1 =[]
residual2 = []

policy1 = []
policy2 = []

value1 = []
value2 = []

# Use BELOW if you want a command line script
#netFile1 = sys.argv[1]
#netFile2 = sys.argv[2]

#rInterp = float(sys.argv[3])
#pInterp = float(sys.argv[4])
#vInterp = float(sys.argv[5])

# WARNING: weight files need to be uncompressed txt files!
netFile1 = "weights_302.txt"
netFile2 = "weights_237.txt"
frankenFile = "weights_302Pol237Val.txt"

rInterp = 1.0
pInterp = 1.0
vInterp = 0.0

def progressBar(count, total, status='', barLen=20):
    fill = int( round( barLen * count / float(total) ) )
    percent = round( 100.0 * count / float(total), 1 )
    bar = '=' * fill + "-" * (barLen - fill)
    sys.stdout.write("\r[%s] [ %s%s ] %s" % (bar, percent, '%', status))
    sys.stdout.flush()

with open(netFile1) as f:
    i = 0
    for line in f.readlines():
        if i < 125: residual1.append([float(x) for x in line.split()])
        elif i < 131: policy1.append([float(x) for x in line.split()])
        else: value1.append([float(x) for x in line.split()])
        progressBar( i, 138, 'Loading ' + netFile1 )
        i += 1
print("\r")
f.close()
        
with open(netFile2) as f:
    i = 0
    for line in f.readlines():
        if i < 125: residual2.append([float(x) for x in line.split()])
        elif i < 131: policy2.append([float(x) for x in line.split()])
        else: value2.append([float(x) for x in line.split()])
        i += 1
        progressBar( i, 138, 'Loading ' + netFile2 )
print("\r")
f.close()

fileOut = open(frankenFile,'w')
fileOut.write( str(residual1[0]).strip("[]").replace(',','') + "\n" )

for i in range(1, len(residual1) ):
    l1 = residual1[i]
    l2 = residual2[i]
    for j in range(0, len(l1)):
        l1[j] = rInterp * l1[j] + (1.0-rInterp) * l2[j]
    progressBar( i, len(residual1)-1, 'Merging Residual' )
    fileOut.write( str(l1).strip("[]").replace(',','') + "\n" )
print("\r")

for i in range(0, len(policy1) ):
    l1 = policy1[i]
    l2 = policy2[i]
    for j in range(0, len(l1)):
        l1[j] = pInterp * l1[j] + (1.0-pInterp) * l2[j]
    progressBar( i, len(policy1)-1, 'Merging Policy' )
    fileOut.write( str(l1).strip("[]").replace(',','') + "\n" )  
    
print("\r")
for i in range(0, len(value1) ):
    l1 = value1[i]
    l2 = value2[i]
    for j in range(0, len(l1)):
        l1[j] = vInterp * l1[j] + (1.0-vInterp) * l2[j]
    progressBar( i, len(value1)-1, 'Merging Value' )
    fileOut.write( str(l1).strip("[]").replace(',','') + "\n" )
    
fileOut.close()    

print("\r")
print("Surgery Complete! Good luck...")
