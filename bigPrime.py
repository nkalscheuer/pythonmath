def getMaxPrime(num):
  i = 2
  while i*i < num:
    while num % i  == 0:
      print(i)
      num = num / i
    i = i + 1
  return num
print (getMaxPrime(600851475143))
