from pprint import pprint
sentence = "A cranky old lady shoots lemons with her high-powered machinegun while wearing crocks."
words = sorted(map(lambda word: word.strip("."), sentence.split(" ")))
results = {}
for word in words:
    first = word[0]
    if first in results:
        results[first].append(word)
    else: 
        results[first]=[]
        results[first].append(word)
pprint(results)    