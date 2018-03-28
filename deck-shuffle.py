# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 15:02:49 2017

@author: jasong
"""

from sys import argv as sys_argv
from csv import DictReader
from random import shuffle

def main(argv):
  file=open('Commander\Slivers!.csv', newline='')
  allrows = DictReader(file)
  
  deck=[]
  
  for row in allrows:
    i=0
    while i<int(row['Count']):
      if 'Creature' in row['Type']:
        typ='Creature'
      elif 'Land' in row['Type']:
        typ='Land'
      else:
        typ=row['Type']
        
      if 'sideboard' not in row['Section']:
        deck.append(typ+': '+row['Name'])
      i+=1
  
  file.close()
  
  n=len(deck)
  
  shuffle(deck)
  for i in range (0,int(n/10)):
    for j in range (0, 10):
      print('   '+deck[10*i+j])
    print('   -----')
  print('')  
  
  
  return True

if __name__ == '__main__':
  main(sys_argv)