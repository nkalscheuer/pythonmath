import re
def testing():
#  print('Working')
  return

def notOp(val):
  return not val
def notStack(stack):
  return not stack.pop()

#ands are working
def andOp(val1, val2):
  return(val1 and val2)
def andStack(stack):
  return andOp(stack.pop(), stack.pop())

#Needs testing/Op working
def orOp(val1, val2):
  return(val1 or val2)
def orStack(stack):
  return orOp(stack.pop(), stack.pop())

#Working/Op working
def ifOp(val1, val2):
  return(not val1 or val2)
def ifStack(stack):
  lastVal = stack.pop()
  return ifOp(stack.pop(), lastVal)

def eqOp(val1, val2):
  return(val1 == val2)
def eqStack(stack):
  return eqOp(stack.pop(), stack.pop())
#End of logical operators

#working
def isOperator(val):
  operators = '[*=\-<>~!+]'
#  print(re.match(operators, val))
  if re.match(operators, val) != None:
    return True
  else:
    return False
#Check if it is a constant:

def isConstBool(val):
  if val.lower() == 'true' or val.lower() == 'false':
    return True
  else:
    return False

def getBoolVal(val):
  if val.lower() == 'true':
    return True
  else:
    return False

def computeStatement(propsVals, input):
  polishStack = []
#  print(propsVals)
  symbolDict = {'*': andStack, '+': orStack, '<=': ifStack, '->': ifStack, '=': eqStack, '!': notStack, '~': notStack }
  for item in input.split():
    if isOperator(item):
      #compute[item](polishStack)
#      print('isOperator, attempting to operate and push return val onto stack')
      polishStack.append(symbolDict[item](polishStack))
    elif isConstBool(item):
      #push getConstBoolVal(item)
#      print('Is boolean constant, pushing bool val onto stack')
      polishStack.append(getBoolVal(item))
#      print('is constant')
    else:
      #polishStack.append(True)
      polishStack.append(propsVals[item])
      #push propsVals[item]
#      print('pushing a val')
  return polishStack[0] 
#print(getLogValDict('Hey Hey n n what the fuck f v n'))
#print(stdin.read().split())
#for word in stdin.read().split():
#print(andOp(True, True))
#print(andOp(False, False))
#print('Or operation:')
#print(orOp(True, False))
#print(orOp(False, False))
#print(orOp(True, True))
#print(ifOp(True, False))
#print('Printing equivalence')
#print(eqOp(True, True))
#print(eqOp(True, False))
#print(notOp(False))
#print(notOp(True))
#  print(word)

#print('Testing regex')
#if re.match('[abc]', 'nnnssdjkndsjne'):
#  print('Matched 1')
#if re.match('[abc]', 'Apple') != None:
#  print('Matched 2')
#if re.match('[abc]', 'aPlle a') != None:
#  print('Matched 33')
#print(isOperator('*'))
#print(isOperator('->'))
#print(isOperator('a'))
#print(isOperator('!'))
#print(isOperator('+'))
#print(isOperator('<='))
#print('ab ' + str(isOperator('ab')))
#print(isOperator('~'))
#print(isOperator('+'))
#print(isOperator('.'))
#print(isConstBool('True'))
#print(isConstBool('FAlse'))
#print(isConstBool('false'))
#print(isConstBool('poop'))
#poopies = [True, False, True]
#print(poopies)
#print(notStack(poopies))
#print(notStack(poopies))
#print(notStack(poopies))
#print(poopies)
#print('and Test')
#poopies = [False, True, False, False, True, False, True, True]
#print(poopies)
#print(andStack(poopies))
#print(andStack(poopies))
#print(andStack(poopies))
#print(andStack(poopies))
#print('Testing if statement')
#poopies = [False, True, False, False, True, False, True, True]
#print(poopies)
#print(ifStack(poopies))
#print(ifStack(poopies))
#print(ifStack(poopies))
#print(ifStack(poopies)) 
