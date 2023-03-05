import collections
from itertools import permutations
import numpy as np
import math

print('''
    __  ___      __       _         ______      __
   /  |/  /___ _/ /______(_)  __   / ____/___ _/ /____
  / /|_/ / __ `/ __/ ___/ / |/_/  / /   / __ `/ / ___/
 / /  / / /_/ / /_/ /  / />  <   / /___/ /_/ / / /__
/_/  /_/\__,_/\__/_/  /_/_/|_|   \____/\__,_/_/\___/ \n
''')


n = int(input("Enter the Order Of matrix 'n' : "))
A = []
A_Row = []
BTemp = []

print("Enter the entries in a line by line (separated by space): \n")

for i in range(1, n+1):
    A.append(list(map(int, input("A"+str(i)+" => ").split())))


for i in A:
    val = sum(i)
    A_Row.append(val)

if (n % 2) == 0:
    BTemp = []
    for BTempPairValue in range(1, round(n/2+1)):
        BTemp.append(BTempPairValue)
        BTemp.append(-BTempPairValue)
else:
    print("Odd condition not works ")
    exit()


def permutation(lst):
    l = []
    for i in range(len(lst)):
        m = lst[i]
        print(m)
    remLst = lst[:i] + lst[i+1:]
    for p in permutation(remLst):
        l.append([m] + p)
    return l

print("\nA(s) => "+str(A_Row))
print("\nB    => "+str(BTemp)+"\n")

li = list(permutations(BTemp))

for B in li:

    result = np.dot(A, list(B))
    c = []
    for i in range(0, len(result)):
        if ((result[i]/A_Row[i]) < 0):
            c.append(math.floor(result[i]/A_Row[i]))
        else:
            c.append(math.ceil(result[i]/A_Row[i]))

    print("A x "+str(B)+" => "+str(result)+" | C => "+str(c))
