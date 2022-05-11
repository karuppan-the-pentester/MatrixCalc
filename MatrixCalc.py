import collections
from itertools import permutations
import numpy as np

n = int(input("Enter the Order Of matrix 'n' : "))
A = []

for i in range(1, n+1):
    exec("%s = []" % ("A"+str(i)))
    for j in range(1, n+1):
        Dynamic_Variable_Name = "A"+str(i)+str(j)
        ElementValue = int(input("A"+str(i)+str(j)+" : "))
        exec("%s.append(%d)" % ("A"+str(i), ElementValue))
    exec("A.append(%s)" % ("A"+str(i)))

if (n % 2) == 0:
    BTemp = []
    for BTempPairValue in range(1, round(n/2+1)):
        BTemp.append(BTempPairValue)
        BTemp.append(-BTempPairValue)
else:
    BTemp = [0]
    for BTempPairValue in range(1, round((n+1)/2)):
        BTemp.append(BTempPairValue)
        BTemp.append(-BTempPairValue)


def permutation(lst):
    l = []
    for i in range(len(lst)):
        m = lst[i]
        print(m)
    remLst = lst[:i] + lst[i+1:]
    for p in permutation(remLst):
        l.append([m] + p)
    return l


li = list(permutations(BTemp))
result = []
for i in range(0, n):
    exec("%s = []" % ("R"+str(i)))
    for j in range(0, n):
        exec("%s.append(0)" % ("R"+str(i)))
    exec("result.append(%s)" % ("R"+str(i)))

MatrixResultChecker = 0

for B in li:
    result = np.dot(A, list(B))
    ZeroChecker = [item for item,
                   count in collections.Counter(result).items() if count > 1]
    if sum(result) == 0 and 0 in result and len(ZeroChecker) == 0:
        print("A x "+str(B)+" => "+str(result))
        MatrixResultChecker = 1

for B in li:
    result = np.dot(A, list(B))
    ZeroChecker = [item for item,
                   count in collections.Counter(result).items() if count > 1]
    if sum(result) == 0 and 0 in result and len(ZeroChecker) == 0:
        print(str(result))

if MatrixResultChecker == 0:
    print("There is no-more value")
