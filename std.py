import sys
from sys import stdin
import re
from itertools import product
import booleanCalculator
#import texttable as tt

#now get it to print a table and you're gewddd
def createTruthTable(input):
  #Preprocess to get variables into dictionary
  logValDict = getLogValDict(input)
  table = []
#  print('Variations:')
  keys = sorted(list(logValDict))
  header = keys
  header.append(input.rstrip('\n'))
  table.append(header)
  for p in product((False, True), repeat=len(logValDict)):
 #   print(p)
    row = list(p)
    #This appends the generated product to the variables in the logdict
    #keys = list(logValDict.keys())
    #print(keys)
    keys = sorted(keys)
    #print(keys)    
    for key, pVal in zip(keys, p):
      #print(pVal)
  #    print(key)
      logValDict[key] = pVal
      #table.append(row)
   # print(logValDict)
   # print(input + ' Output:')
    row.append(booleanCalculator.computeStatement(logValDict, input))
    table.append(row)
  return table


#booleanCalculator.testing()

def getLogValDict(input):
  dict = {}
  for word in input.split():
    if not booleanCalculator.isOperator(word) and not booleanCalculator.isConstBool(word):
     dict[word] = 0
  return(dict)

def printTruthTable(table):
  for row in table:
#    print(row)
    rowStr = ''
    for item in row:
      rowStr = rowStr + str(item) + ' '
    print(rowStr)
    

#def rowBuilderString(row):
 # rowBuilder = ''
  #print('{:10}'.format(row*))
  
      
##The above is probably unnecessary in this file, but im using it for testing ahahah
testInput = 'p q False s -> * *'
testInput = stdin.read()
#print(testInput)
#print(createTruthTable(testInput))
printTruthTable(createTruthTable(testInput))          
#print(booleanCalculator.computeStatement({'p': True, 'q': False}, 'p q ->'))
#print(booleanCalculator.computeStatement({'p': True, 'q': True},  'p q ->'))
#print(getLogValDict('Hey Hey n n what the fuck f v n'))
#print(stdin.read().split())
#for word in stdin.read().split():

