import random


def weighted_choice(choices):
    total = sum(range(0,len(choices)+1))
    r = random.uniform(0, total)
    tot = 0
    for c in range(1, len(choices)+1):
        if tot + c >= r:
            return choices[c-1]
        tot += c
    assert False, "Shouldn't get here"

a = ['a','b','c','d','e']
ans = [0,0,0,0,0]

for snu in range(0, 100):
    tmp = weighted_choice(a)
    if tmp == 'a': ans[0] += 1
    if tmp == 'b': ans[1] += 1
    if tmp == 'c': ans[2] += 1
    if tmp == 'd': ans[3] += 1
    if tmp == 'e': ans[4] += 1

for key in ans:
    print(key)
