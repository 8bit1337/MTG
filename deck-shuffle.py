# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 15:02:49 2017

@author: jasong
"""

from sys import argv as sys_argv
from csv import DictReader
from random import shuffle

#For plotting the bar charts of possible land counts
import numpy as np
import matplotlib.pyplot as plt

def main(argv):
#  file=open('Precon\Breed Lethality.csv', newline='')
  file=open('Regular\Dragons!.csv', newline='')
  allrows = DictReader(file)
  
  deck=[]
  landcount=0
  for row in allrows:
    i=0
    
    while i<int(row['Count']):
      if 'Creature' in row['Type']:
        typ='Creature'
      elif 'Land' in row['Type']:
        typ='Land'
        landcount+=1
      else:
        typ=row['Type']
        
      if 'sideboard' not in row['Section']:
        deck.append(typ+': '+row['Name'])
      i+=1
  
  file.close()

  land=0
  iterations=20000
  tarmana=5
  opencount=np.zeros(8, dtype=int)
  targetlands=np.zeros(8, dtype=int)

  for i in range(0,iterations):
    shuffle(deck)
    count=0
    for c in range (0,7):
      if deck[c][:4]=='Land':
        count+=1
    opencount[count]+=1
    land+=count
    
    draw=0
    while count<tarmana:
      c+=1
      draw+=1
      
      if deck[c][:4]=='Land':
        count+=1
      
    if draw>7:
      draw=7
    targetlands[draw]+=1
  
  opencount=opencount/iterations

  #draw a graph of haw much mana we get in the first hand
  plt.bar(range(len(opencount)), opencount, .75, color="blue", index=1)
  for i in range(8):
    plt.text(i-.2, opencount[i]+.002, "{0:.0%}".format(opencount[i]))

  plt.text(6.5, max(opencount)-.002, 'Land: ' + str(landcount))
  plt.text(6.5, max(opencount)-.027, 'Avg: ' + str(round(land/iterations,1)))
  
  #draw a graph of how long it takes to get to our target mana figure
  plt.bar(range(len(targetlands)), targetlands, .75, color="red", index=2)
  for i in range(len(targetlands)):
    plt.text(i-.2, targetlands[i]+.002, "{0:.0%}".format(targetlands[i]))
  
  
  
  return True

if __name__ == '__main__':
  main(sys_argv)