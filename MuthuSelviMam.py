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
A_Row = []
BTemp = []

print("Enter the entries in a line by line (separated by space): \n")

for i in range(1, n+1):
    A.append(list(map(int, input("A"+str(i)+" => ").split())))
    

for i in A:
    val=sum(i)
    A_Row.append(val)
    
if (n % 2) == 0:
    BTemp = []
    for BTempPairValue in range(1, round(n/2+1)):
        BTemp.append(BTempPairValue)
        BTemp.append(-BTempPairValue)
else:
    print("Odd condition not works ")
    exit()

print("\nA1 => "+str(A)+"\n")
print("\nB1 => "+str(BTemp)+"\n")

result = np.dot(A, list(BTemp))
print(result)

c=[]
for j in range(n):
    for i in result:
        print(str(i)+" => "+str(j))
    