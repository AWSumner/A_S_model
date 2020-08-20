#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 14:53:58 2020

@author: sumphys
"""
import copy
import numpy as np 
import time 
import math 
import random
from Functions import Stepping_Functions as SF
from Functions import Starting_conditions as SC 

size=2000
print(size)
OG_time = time.time()
'''

print('Zero make')
start_time = time.time()
M1=np.array([[0 for q in range(size)] for r in range(size)]) #makes an maxis with all zeros
M2=np.array([[0 for q in range(size)] for r in range(size)]) #makes an maxis with all zeros
print("--- %s seconds ---" % (time.time() - start_time))

print('Rand make')
new_time2=time.time()
M3=np.array([[random.uniform(0,2*np.pi) for q in range(size)] for r in range(size)]) #makes an maxis with all zeros
M4=np.array([[random.uniform(0,2*np.pi) for q in range(size)] for r in range(size)]) #makes an maxis with all zeros
print("--- %s seconds ---" % (time.time() - new_time2))


Map=[[0,1,2,3,4,5],[5,4,3,2,1,0],[5,6,7,8,9,0],[0,9,8,7,6,5],[1,3,5,7,9,3],[2,4,6,8,4]]

M=Map[2:5]

#print(M)
print('Cut speed')
point=[size/2,size/2]
new_time9=time.time()
new=SF.Map_Cut(M3,[size/2,size/2],100)[0]
print("--- %s seconds ---" % (time.time() - new_time9))
#print(len(new),len(new[0]),point)

#sites=[[0,1],[2,3],[4,5]]
#inverse=[0,2]
#test=SF.Conversion(sites, inverse)
#print(test)


print("Rand Mult")
new_time3=time.time()
mult1=np.multiply(M3,M4)
print("--- %s seconds ---" % (time.time() - new_time3))

print('Zero mult')
new_time1=time.time()
mult1=np.multiply(M1,M2)
print("--- %s seconds ---" % (time.time() - new_time1))


print("Rand dot")
new_time4=time.time()
mult1=M1 @ M2
print("--- %s seconds ---" % (time.time() - new_time4))

print('Zero dot')
new_time5=time.time()
mult1=M1 @ M2
print("--- %s seconds ---" % (time.time() - new_time5))


print('Done')

'''

'''
Map=[[0,0,0,0,0,0],[0,0,1,0,0,0],[0,0,0,0,0,0],[0,0,1,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
Map2=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,1,0,0,0],[0,0,0,0,0,0],[0,0,1,0,0,0]]
Map3=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[1,0,1,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
Plist=[[2,1],[4,3],[0,3],[2,5]]
trials=1000000
print(np.array(Map))
Heads=SC.Head_Locations([2,3],Map,2,0)
'''
'''
for i in range (trials):
    Heads=SC.Head_Locations([2,3],Map,2,0)
    n=0
    if Heads[1] not in Plist:
        print('There was an error')
        print('H2 was')
        print(Heads[1])
        n=1
        break
if n==0:
    print("No errors!")
print("--- %s seconds ---" % (time.time() - OG_time))
#print([np.array([0,3])])

Beads=[]
n=0
new_time3=time.time()
for i in range (trials):
    #print(Heads[0],Heads[1])
    Bead=SC.Bead_Placement(Heads[0],Heads[1],1,True,10,20,2)
    
    if Bead not in Beads: 
        Beads.append(Bead)
    if len(Beads)>4:
        print('There was an error')
        n=1
        break
        
    
if n==0:
    print('Consistent')
print(Beads)


print("--- %s seconds ---" % (time.time() - new_time3))
'''

'Class definition'
class motor(): #creates a class of motor
    #shared properties in all motors 
    
    
    #unique properties for each instance of motor()
    def __init__(self,Head_1,Head_2,Attachment): 
        self.H1=Head_1 #informations for head 1
        self.H2=Head_2   #information on head 2
        self.At=Attachment #location of the connection to the bead
    
    
class MVI(motor): #Myosin VI motor
    '''Makes a class that inherets motors and can have additional properies that are unique to myosin VI
        This extension will allow for possible expansion to different motors 
    '''  
    Al=36 #nm :arm length
    SP=20 #nm : rest length of spring
    


Map=[[0,0,0,0,0,0],[0,0,1,0,0,0],[0,0,0,0,0,0],[0,0,1,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
#print(Map[1][2])


M=motor([0,1],[4,3],[0,3])
 
#print(M.H1,M.H2)   
mass=copy.deepcopy(M.H1)
cat=M.H1
#print(cat)
M.H1=M.H2
M.H2=mass
#print(cat)
#print(M.H1,M.H2)   
'Initial conditions '

k=np.array([[1,2],[3,4],[1,1]])
j=np.append([0,1],k)
print(j) 























