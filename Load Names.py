from random import randint

adj = tuple(open('adjectives.txt', 'r'))
nouns = tuple(open('nouns.txt', 'r'))
verbs = tuple(open('verbs.txt', 'r'))


def names():
    #verbPick = verbs[randint(0, 761)].capitalize().splitlines()[0]
    adjPick = adj[randint(0, 626)].capitalize().splitlines()[0]
    nounPick = nouns[randint(0, 2453)].capitalize().splitlines()[0]
    return adjPick+" "+nounPick


for i in range(10):
    print(names())
