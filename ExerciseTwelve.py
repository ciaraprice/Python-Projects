#lotto script that displays 6 unique random lottery numbers between 1-50.
import random
lottoSet = set([])

while len(lottoSet) < 6:
    lottoSet.add(random.randint(1, 50))
print(lottoSet, len(lottoSet))
