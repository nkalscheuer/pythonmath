#vorking
#these arent the most optimized, but I just wanted to play code golf and get em in one line lol
def is_reflexive(Set, Relation):
  return {(i,i) for i in Set}.issubset(Relation)

def is_symmetric(Relation):
  return {(y,x) for (x,y) in Relation}.issubset(Relation)

def removingpairs(Relation):
  return {(x,y) for (x,y) in Relation if x != y} 

#vorking
def is_antisymmetric(Relation):
  return not set((x,y) for (x,y) in Relation if (x != y and (y, x) in Relation))

def is_transitive(Relations):
  return not set((x,y) for (x,y) in Relations if {(a,b) for (a,b) in Relations if b == x and not {(c,d) for (c,d) in Relations if c == a and d == y}})

def composite(R1, R2):
  return {(item1[0],item2[1]) for item1 in R1 for item2 in R2 if item1[1] == item2[0]}

def is_equivalence(Set, Relation):
  return is_reflexive(Set, Relation) and is_symmetric(Relation) and is_transitive(Relation)






