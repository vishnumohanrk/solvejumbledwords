import itertools as it
import enchant as ec

dic = ec.Dict('en_US')
word = input()

for i in (iter(it.permutations(word,len(word)))):
    res = ''.join(list(i))
    if (dic.check(res)):
        print(res)
    else:
        pass