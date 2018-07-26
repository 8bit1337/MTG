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
  lands=0
  for row in allrows:
    i=0
    
    while i<int(row['Count']):
      if 'Creature' in row['Type']:
        typ='Creature'
      elif 'Land' in row['Type']:
        typ='Land'
        lands+=1
      else:
        typ=row['Type']
        
      if 'sideboard' not in row['Section']:
        deck.append(typ+': '+row['Name'])
      i+=1
  
  file.close()
    
  counts=np.zeros(8, dtype=int)
  land=0
  iterations=10000
  for i in range(0,iterations):
    shuffle(deck)
    count=0
    for c in range (0,7):
      if deck[c][:4]=='Land':
        count+=1
    counts[count]+=1
    land+=count
  
  
  counts=counts/iterations
  plt.bar(range(8), counts, .75, color="blue")
  for i in range(8):
    plt.text(i-.2, counts[i]+.002, "{0:.0%}".format(counts[i]))

  plt.text(6.5, max(counts)-.002, 'Land: ' + str(lands))
  plt.text(6.5, max(counts)-.027, 'Avg: ' + str(round(land/iterations,1)))
  
  
  
  return True

if __name__ == '__main__':
  main(sys_argv)