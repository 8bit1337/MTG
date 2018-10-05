# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 15:02:49 2017

@author: jasong
"""

from sys import argv as sys_argv
from csv import DictReader,writer
from random import shuffle

def main(argv):
  #open the csv and import all of the rows
  with open('Regular\Dragons!.csv', newline='') as readcsv:
    allrows = DictReader(readcsv)
    x=1
    order=[]
    card=[]
    tipe=[]
    cost=[]
    for row in allrows:
      if 'sideboard' in row['Section']:
          continue
      for c in range(int(row['Count'])):
        order.append(x)
        card.append(" ".join(row['Name'].split()))
        tipe.append(" ".join(row['Type'].split()))
        cost.append(row['Cost'])
        x+=1

  iterations=10000
  with open('simulations.csv', 'w') as writecsv:
    output = writer(writecsv, lineterminator='\n') #,quotechar='|')
    output.writerow(['Iteration|Order|Card|Type|Cost'])
    
    for i in range(iterations):
      shuffle(order)
      
      #Count,Name,Type,Cost,Rarity,Section
      for x in range(len(order)):
        output.writerow([str(i+1)+'|'+str(order[x])+'|'+card[x]+'|'+tipe[x]+'|'+cost[x]]) 
          
  return True

if __name__ == '__main__':
  main(sys_argv)