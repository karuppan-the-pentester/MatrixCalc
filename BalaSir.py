import collections
from itertools import permutations
import numpy as np

print('''
    __  ___      __       _         ______      __    
   /  |/  /___ _/ /______(_)  __   / ____/___ _/ /____
  / /|_/ / __ `/ __/ ___/ / |/_/  / /   / __ `/ / ___/
 / /  / / /_/ / /_/ /  / />  <   / /___/ /_/ / / /__  
/_/  /_/\__,_/\__/_/  /_/_/|_|   \____/\__,_/_/\___/ \n
''')
n = int(input("Enter the Order Of matrix 'n' : "))
A = []
ResultMatrix=[]
try:
    print("Enter the entries in a line by line (separated by space): \n")
    for i in range(1, n+1):
        A.append(list(map(int, input("A"+str(i)+" => ").split())))

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

    print("\nB1 => "+str(BTemp)+"\n")

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

    MatrixResultChecker = 0
    for B in li:
        result = np.dot(A, list(B))
        ZeroChecker = [item for item,
                       count in collections.Counter(result).items() if count > 1]
        if (n % 2) == 0:
            if sum(result) == 0 and 0 not in result and result not in ResultMatrix:
                print("A x "+str(B)+" => "+str(result))
                MatrixResultChecker = 1
                ResultMatrix.append(result)
        else:
            if sum(result) == 0 and 0 in result and len(ZeroChecker) == 0 and result not in ResultMatrix:
                print("A x "+str(B)+" => "+str(result))
                MatrixResultChecker = 1
                ResultMatrix.append(result)
    print("\n")
    internalcheck=0
    for B in li:
        result = np.dot(A, list(B))
        ZeroChecker = [item for item,
                       count in collections.Counter(result).items() if count > 1]
        for i in result:
            if (i and -i in result):
                internalcheck = internalcheck + 1
        if (n % 2) == 0:
            if sum(result) == 0 and 0 not in result and result not in ResultMatrix and internalcheck==n:
                print(str(result))

        else:
            if sum(result) == 0 and 0 in result and len(ZeroChecker) == 0 and result not in ResultMatrix and internalcheck==n:
                print(str(result))

    if MatrixResultChecker == 0:
        print("\nThere is no-more value")

except Exception as e:
    print("The code contains Bug")
    print(e)
