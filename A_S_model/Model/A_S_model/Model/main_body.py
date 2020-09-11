# -*- coding: utf-8 -*-
'''
Overview
this is there I will put the code descirption once I have made it

'''

'Stock imports & constants '
import csv 
import numpy as np 
import math 
import os.path 
import random
import time

start_time = time.time() #added a timer because it is fun

'Import my functions '
from Functions import Stepping_Functions as SF
from Functions import Dwell as D
from Functions import Starting_conditions as SC
from Functions import Landing_functions as LF


'File choices'
Map_name='Test_072820_1.csv' #name of map file
Output_file=0 #name of output file to save some results


' Modifiable values and force toggling '
number_of_motors=1 #total number of motors to attach to the bead
radial_placement= True #is the placement of motors on the bead random (True) or evenly distributed (False)
placement_coordinates=False #choice of placement locations if "False" it will place randomly 
bead_radius=10 #nm, the radius of the bead motor are attached to. 
optical_trap=False # 
time=60 #s, total amout of time the model will run over in seconds (converted to milisecond time intervals further down)
error=4 #the value of the +- bars on the search range

'Physical constants'
kf=0.16 #pN/nm: the k value for the torsion force
ks=0.2 #pN/nm: the k value for the spring

'Class definition'
class protien_motor(): #creates a class of motor
    #shared properties in all motors 
    Cm=[0,0]
    
    #unique properties for each instance of motor()
    def __init__(self,Head_1,Head_2,Attachment): 
        self.H1=Head_1 #informations for head 1 (array)
        self.H2=Head_2   #information on head 2 (array)
        self.At=Attachment #location of the connection to the bead (array)
    
    
class MVI(protien_motor): #Myosin VI motor
    '''Makes a class that inherets from protien motor 
       and can have additional properies that are unique to myosin VI
    '''  
    Al=36 #nm :arm length
    'VVV currently a place holder value!!!! VVV'
    Sl=20 #nm : rest length of spring 
    '^^^ currently a place holder value!!!! ^^^'

'Opening map'
map_path='./Reference/Maps/' #Path to the map file note: code needs to be run in A_S_model folder (see top right)
Map_file=os.path.join(map_path,Map_name) #adds the name to the path

with open(Map_file, newline='') as f:
    reader = csv.reader(f)
    Map = list(reader) #creates an array Map that holds the values for each pixel. 
    


'Initial conditions '
Lstep=MVI.Al #step length
Lspring=MVI.Sl#rest length of spring
Heads=SC.Heads_Placement(placement_coordinates,Map,Lstep,error) #decides the location of the two starting head locations
Bead_attachments=SC.Bead_Placement(Heads[0], Heads[1], number_of_motors, radial_placement,bead_radius, Lspring, Lstep)[0] #creates the list of bead attachment points



'Creating motors'
motor_list=[] #reset motor list

number_of_motors=2 #easy editing for testing
test_conditions=[[[0,0],[0,36],[0,42]],[[0,1],[0,32],[0,52]]] #a list of initial conditions for testing

for i in range(number_of_motors): #creates a motors based on the number given at the start
    var=test_conditions[i] #pulls out the inital conditions for each motor 
    m=MVI(var[0],var[1],var[2]) #adds the inital conditions to each motor (H1,H2,At)
    motor_list.append(m) #adds each motor to the list of all motors for future reference
    
#print(All_motors)    
#print(All_motors[0].H1)


'Core code '
total_time=time*1E3 #converitng the time above in seconds to miliseconds to match our timesteps


for i in range(total_time):
    
    'Motor step section'
    for motor in motor_list:
        
        D=D.Dewll() #returns a bolean that will tell if this particular motor steps this loop
        # will add stuff to the motor to deal with the dwell time 
        if D:      
            locations=SF.Step(Map,motor.H1,motor.Al,error) #looks on the map for possible locations and reurns an array
            Potentials=[]
            for item in locations:
                'Center of mass '
                CMX=(motor.H1[0]+item[0])/2 #computes the CM for theis paticular location in x
                CMY=(motor.H1[1]+item[1])/2 #computes the CM for theis paticular location in y
                Cm=[CMX,CMY] #CM location as an array
                'Theta section'
                theta_CM=SF.Angle_Calc(motor.H1,item,motor.Al)
                theta_H1=Map[motor.H1[1]][motor.H1[0]]
                theta_H2=Map[item[1]][item[0]]
                
                dtheta_H1=abs((theta_CM)-(theta_H1))
                dtheta_H2=abs((theta_CM)-(theta_H2))
                
                'Potentials'
                Pt=LF.MIV_Potential(dtheta_H1, dtheta_H2, Cm, motor.At,kf,ks)# calclulates the potential to land there
                Potentials.append(Pt) #add it to the list
            
            motor.H2=LF.Landing_probability(locations, Potentials)
            
            'Swapping lead and trailing head '
            CMX=(motor.H1[0]+motor.H2[0])/2 #computes the CM in the x direction
            CMY=(motor.H1[1]+motor.H2[1])/2 #computes the CM in the y direction
            
            motor.CM=[CMX,CMY]
            H1_copy=motor.H1 #creates a copy of H1 for use below
            motor.H1=motor.H2 #swaps H1 value with H2
            motor.H2=H1_copy #Makes H2 be equal to the copy of H1
            
            
            'Resource update'
            #this section will be for modifying resources that the Dwell will read
            
        else: 
            #nothing else in here until we add factors relating to dwell time
              print('hi')
        
    
    '"Force" & Bead update section'
    dx_list=[]
    dy_list=[]
    for motor in motor_list:   
        
        X_diff=(motor.Cm[0]-motor.At[0]) 
        Y_diff=(motor.Cm[1]-motor.At[1])
        angle=math.atan(Y_diff/X_diff) # the equilibrium angle
        
        dx=motor.Sl*np.cos(angle)-abs(X_diff) #computed the x 
        dy=motor.Sl*np.sin(angle)-abs(Y_diff) #computed the y 
        
        dx_list.append(dx) #add it to the list
        dy_list.append(dx) #add it to the list
     
        
    update_x=sum(np.array(dx_list))/len(dx_list) #net change in x direction
    update_y=sum(np.array(dy_list))/len(dy_list) #net change in y direction
    
    'Applying change '
    for motor in motor_list: #makes sure the attachment points are updated for each motor
    
        x_pos=motor.At[0]+update_x #takes the calcluated change in x and applies it to each motor
        y_pos=motor.At[1]+update_y #takes the calculated change in y and applies it to each motor
        motor.At=[x_pos,y_pos] #changed the attackment point to the new location
        
    

'Visualization'




print('Done') 
print("--- %s seconds ---" % (time.time() - start_time)) #see timers are fun!


'Testing '



