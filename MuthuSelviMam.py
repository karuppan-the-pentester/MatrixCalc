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
BTemp = []

print("Enter the entries in a line by line (separated by space): \n")

for i in range(1, n+1):
    A.append(list(map(int, input("A"+str(i)+" => ").split())))

for i in range(1, n+1):
    BTemp.append(list(map(int, input("B"+str(i)+" => ").split())))


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
print(li)
# for B in li:
#     result = np.dot(A, list(B))
#     ZeroChecker = [item for item,
#                    count in collections.Counter(result).items() if count > 1]
#     print(ZeroChecker)
# print("\n")
