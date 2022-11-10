# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 05:11:49 2022

@author: Jon


make a dictionary the contains 'Family' members
(Family in quotes because I do not want real name or birthday... make them),
at least 5 'immediate' family members.   

object for each member contains birthday (string),
favorite color,
favorite recording artist(s)

1. print the dictionary

2. add an entry for new member of the family (no recording artist)

3 print values for member of the family whose name string
starts with whoever is first in the alphabet


"""


FamMbrs = {'Ted' : ['1/1/1991', 'grey', 'Elvis']}
FamMbrs ['Bill'] = ['2/2/1992', 'purple', 'Queen']
FamMbrs ['Skyler'] = ['3/3/1993', 'blue', 'The Beatles']
FamMbrs ['Walter'] = ['4/4/1994', 'white', 'The Who']
FamMbrs ['Joe'] = ['5/5/1995', 'orange', 'Nirvana']
FamMbrs ['Bob'] = ['6/6/1996', 'red', 'Led Zeppelin']

#1. print the dictionary

print(FamMbrs)

#2. add an entry for new member of the family (no recording artist)

FamMbrs ['Marshall'] = ['7/7/1997', 'blue']
print('\n', FamMbrs, '\n')

#3 print values for member of the family whose name string
#starts with whoever is first in the alphabet

print(FamMbrs[sorted(FamMbrs.keys())[0]])