from random import randint

adj = tuple(open('adjectives.txt', 'r'))
nouns = tuple(open('nouns.txt', 'r'))
verbs = tuple(open('verbs.txt', 'r'))


def names():
    first = verbs[randint(0, 761)].capitalize().splitlines()[0]
    second = adj[randint(0, 626)].capitalize().splitlines()[0]
    third = nouns[randint(0, 2453)].capitalize().splitlines()[0]
    return first+" "+second+" "+third


for i in range(10):
    print(names())
