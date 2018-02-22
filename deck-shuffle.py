# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 15:02:49 2017

@author: jasong
"""

from sys import argv as sys_argv
from csv import DictReader
from random import shuffle

def main(argv):
  file=open('Commander\Slivers.csv', newline='')
  allrows = DictReader(file)
  deck=[]
  print('Importing Deck...')
  for row in allrows:
    i=0
    while i<int(row['Count']):
      if 'Creature' in row['Type']:
        typ='Creature'
      else:
        typ=row['Type']
      deck.append(typ+': '+row['Name'])
      i+=1
  
  print('Done') 
  
  draw=1
  while draw<=3:
    print('Draw: ')  
    shuffle(deck)
    for i in range (0, 7):
      print('   '+deck[i])
    print('   -----')
    for i in range(7, 10):
      print('   '+deck[i])
    draw+=1
    print('')  
  
  file.close()
  return True

if __name__ == '__main__':
  main(sys_argv)