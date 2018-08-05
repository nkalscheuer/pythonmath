
def isPrime(num):
  poop = int(num**0.5)
  if num%poop == 0:
    return False
  counter = 2
  while counter < poop:
    if num%counter == 0:
      return False
    counter = counter + 1
  return True


def getLargestPrime(number):
  #counter = int(number**0.5)
#  factors = list(i for i in range(int(number/2)) if number%i == 0)
  #print('list generated')
  #counter = int(number/2)
  for i in range(int(number/2), 1, -1):
    if number%i == 0:
      if isPrime(i):
        return i
    #counter = counter - 1
    #print("counter:")
    #print(counter)
  #return counter
print(getLargestPrime(600851475143))
print(isPrime(3))
print(isPrime(4))    
