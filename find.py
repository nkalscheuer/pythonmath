mport sys
import fileinput
import re
presidentsSet = set()
trumpSet = set()
trumpWordCounter = 0
pattern = '(?:[A-Z]\.)+[A-Z]?[a-zA-Z\']+)'
for line in fileinput.input():
    if(fileinput.filename() == sys.argv[len(sys.argv) - 1]):
        for word in re.findall(pattern, line):
            if word is not None and word != " ":
                trumpSet.add(word.lower())
                trumpWordCounter = trumpWordCounter + 1
    else:
        for word in re.findall('pattern| ', line):
            if word is not None and word != " ":
                presidentsSet.add(word.lower())
sortedUnique = list(trumpSet - presidentsSet)
sortedUnique.sort()
for item in sortedUnique:
    print(item)
print("Unique words in trumps speech (not in others): " + str(len(sortedUnique)) )

print(len(trumpSet))
print(len(presidentsSet) + len(trumpSet))
print(sys.argv[len(sys.argv) - 1])
print(trumpWordCounter)
print(trumpSet - presidentsSet)
