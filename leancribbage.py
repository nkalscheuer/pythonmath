import itertools
import sys

def rankVal(rank):
	if rank in list('JQK'):
		return 10
	return list('A23456789T').index(rank) + 1

def isStraight(cards):
	for x in range(0, len(cards)):
		if rankVal(cards[0][0]) + x != rankVal(cards[x][0]):
			return False
	return True

def isFlush(hand):
	return not {x for x in hand if list(hand)[0][1] != x[1]}
	
def getStraights(straightLength, hand):
	return {x for x in itertools.permutations(hand, straightLength) if isStraight(x)}


def __main__():
	hand = {tuple(list(sys.argv[x])) for x in range(1, 6)}
	nob = tuple(list(sys.argv[1]))
	#print(list(itertools.combinations(hand, 2)))
	pairs = set((x[0], x[1]) for x in itertools.combinations(hand, 2) if x[0][0] == x[1][0])
	fifteens = set(x for r in range(2, 6) for x in itertools.combinations(hand, r) if sum(list(rankVal(i[0]) for i in x)) == 15)
	fivestraights = getStraights(5, hand)
	fourstraights = getStraights(4, hand)
	threestraights = getStraights(3, hand)
	fiveflush = isFlush(hand)
	fourflush = isFlush(hand - {nob})
	knobjack = int(('J', nob[1]) in hand)
	print('Knob jack: ' + str(knobjack))
	print('Four flush: ' + str(fourflush))
	print('Five flush: ' + str(fiveflush))
	print('Threestraights:')
	print(threestraights)
	print('fifteens:')
	print(fifteens)
	print('hand:')
	print(hand)
	print('pairs:')
	print(pairs)
	print(len(pairs))
	print('Is Flush? ' + str(isFlush(hand)))
	print(1 == rankVal('A'))
	print(2 == rankVal('2'))
	score = 2*len(fifteens) 
	score += 2*len(pairs) 
	score += knobjack 
	score += 5*len(fivestraights) 
	score += 4*(len(fourstraights)*(len(fivestraights) == 0)) 
	score += 3*(len(fourstraights) == 0)*len(threestraights) 
	score += 5*int(fiveflush) 
	score += int(not fiveflush)*(fourflush)
	print(score)
__main__()
