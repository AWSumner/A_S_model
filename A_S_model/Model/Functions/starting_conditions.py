#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 17:19:52 2020

@author: sumphys
"""

import numpy as np 
import math 
import random
import random


def Head_Locations(P_C,Map):
    
    if P_C == False: 
        H1=0
    
    else: 
        H1=P_C

    #add a  version of a walking search for the H2 bit
    H2=0
    return(H1,H2)
    
    
     
def Bead_Placement(H1,H2,Number_of_Motors,Radial_Placment,r):
    phi=[]
    if Radial_Placment ==True: 
        
        for i in range(Number_of_Motors):
            temp=random.uniform(0,2*np.pi)
            phi.append(temp)           
    else:
        for i in range(Number_of_Motors):
            temp=i*2*np.pi/Number_of_Motors
            phi.append(temp)
    
    Hx=H1[0]-H2[0]
    Hy=H1[1]-H2[1]
    theta=2*np.pi-math.asin(Hx/36)
    attachment_list=[]
    
    point=[0,0]
    attachment_list.append(point)
    
    for i in range(Number_of_Motors):
       x=r-r*math.cos(phi[i])
       y=r*math.sin(phi[i])
       dx=x*math.cos(theta)-y*math.sin(theta)
       dy=x*math.sin(theta)+y*math.cos(theta)
       location=[point[0]+dx,point[1]+dy]
       attachment_list.append(location)
       
    
       
       
       print('hi')
    
    
    return(phi)

