# -*- coding: utf-8 -*-
'''
Overview
this is there I will put the code descirption once I have made it

'''

'Stock imports & constants '
import numpy as np 
import math 
import random
import os.path 
import csv 

'Import my functions '
from Functions import Step_functions as SF
from Functions import Dwell as D
from Functions import starting_conditions as S_C

'File choices'
Map_name='Test_072820_1.csv' #name of map file
Output_file=0

' Changing values and force toggling '
number_of_motors=1 #total number of motors to attach to the bead
radial_placement= True #is the placement of motors on the bead random (True) or evenly distributed (False)
placement_coordinates=False #choice of placement locations if "False" it will place randomly 
bead_radius=10 #nm, the radius of the bead motor are attached to. 
optical_trap=False # 
second_time=60 #s, total amout of time the model will run over in seconds 
              #(converted to milisecond time intervals further down)

'Class definition'
class motor(): 
    #shared properties in all motors 
    Al=36 #nm #arm length
    
    #unique properties for each instance of motor()
    def __init__(self,Head_1,Head_2,Attachment): 
        self.H1=Head_1 #informations for head 1
        self.H2=Head_2   #information on head 2
        self.At=Attachment #location of the connection to the bead
        

'Opening map'
map_path='./Reference/Maps/' #Path to the map file note: code needs to be run in A_S_model folder (see top right)
Map_file=os.path.join(map_path,Map_name) #adds the name to the path

with open(Map_file, newline='') as f:
    reader = csv.reader(f)
    Map = list(reader) #creates an array Map that holds the values for each pixel. 

'Conditions creation'
loc=S_C.Starting_Location(placement_coordinates,Map)




'Creating motors'
All_motors=[] #reset motor list

number_of_motors=2 #easy editing for testing
test_conditions=[[[0,0],[0,36],[0,42]],[[0,1],[0,32],[0,52]]] #a list of initial conditions for testing

for i in range(number_of_motors): #creates a motors based on the number given at the start
    var=test_conditions[i] #pulls out the inital conditions for each motor 
    m=motor(var[0],var[1],var[2]) #adds the inital conditions to each motor (H1,H2,At)
    All_motors.append(m) #adds each motor to the list of all motors for future reference
    
#print(All_motors)    
#print(All_motors[0].H1)


'Core code '
total_time=second_time*1E3 #converitng the time above in seconds to miliseconds to match our timesteps






'Visualization'






print('Done')
'Testing '

'''
'See possible imports'
import pkgutil
search_path = ['.'] # set to None to see all modules importable from sys.path
all_modules = [x[1] for x in pkgutil.iter_modules(path=search_path)]
print(all_modules)

#print(sys.path)
#x=dir(running) #r.fib(8)
#print(x)
'''

