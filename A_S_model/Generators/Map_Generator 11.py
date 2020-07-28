#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 14:47:17 2020

@author: sumphys
"""
'''Overview: 


'''
'Imports & functions'
from PIL import Image

def Sum(a):
    total=0
    for i in range(0,len(a)):
        total+=a[i]
    return(total)


'File selection'

im=Image.open('./Reference/Images/Test.png') 
'Note: As this file is in Generators one dot take you up one directory to A_S_model. '
'IMPORTANT NOTE: you will need to change the name of file you are making at the bottom for this to work'
     

'Reading RGB and values'

pix    =im.load() #Actually load the file to process
width  =im.size[0] #x dimension in pixels
height =im.size[1] #y dimension in pixels

'Note: pix[x,y] is the RGB value of the pixel at a point (x,y)'


'Map construction'
c=0.2356 #this is the conversion constant between the sum of the RGB and the corrisponding angle 
        # tunes so a total sum of RGB munius one (764) produces close to 180 deg. 

total_map=[] #reset for total map
for n in range(0,height):
    row=[] #reset for the next row
    for i in range(0,width):
        RGB=Sum(pix[i,n])
        
        if RGB==765:
            theta=-1 #sets theta to -1 to indicate not part of the actin network
        else:
            theta=c*RGB #converts RGB to the theta. 
               
        element=[i,n,theta]
        row.append(element)
        
    total_map.append(row)

'Writing to a file'
with open('listfile.txt', 'x') as filehandle:
    filehandle.writelines("%s\n" % k for k in total_map)
    
'Test'
'''
im.show()
'''