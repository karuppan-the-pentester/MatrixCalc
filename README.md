# Matrix Calculator

[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

This program was created by [Karuppasamy K](https://github.com/karuppan-the-pentester/)

[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/karuppan-the-pentester/)
[![Google](https://img.shields.io/badge/google-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://www.google.com/search?q=karuppan+the+pentester)
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://in.linkedin.com/in/karuppasamy-k-308a13200)
[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white)](https://www.instagram.com/karuppan_the_pentester/)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:karuppan.the.pentester@gmail.com)

This [program](https://github.com/karuppan-the-pentester/MatrixCalc/blob/master/MatrixCalc.py) will give the desired output you given

```python
import collections
from itertools import permutations
import numpy as np
```

This part shows that what are the modules we used in the program

```python
n = int(input("Enter the Order Of matrix 'n' : "))
A = []
```

This part of the program represent the input we get from the user about the order of the matrix  
And creating an empty array A

```python
for i in range(1, n+1):
    exec("%s = []" % ("A"+str(i)))
    for j in range(1, n+1):
        Dynamic_Variable_Name = "A"+str(i)+str(j)
        ElementValue = int(input("A"+str(i)+str(j)+" : "))
        exec("%s.append(%d)" % ("A"+str(i), ElementValue))
    exec("A.append(%s)" % ("A"+str(i)))
```

This part of the program is used to get the elements of the A matrix as input from the user

```python
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
```

This part of the program create the B1 matrix from the order of matrix based on the odd or event condition you gave us

```python
def permutation(lst):
    l = []
    for i in range(len(lst)):
        m = lst[i]
        print(m)
    remLst = lst[:i] + lst[i+1:]
    for p in permutation(remLst):
        l.append([m] + p)
    return l
```

This function creates an multiple combination of B1

```python
li = list(permutations(BTemp))
result = []
for i in range(0, n):
    exec("%s = []" % ("R"+str(i)))
    for j in range(0, n):
        exec("%s.append(0)" % ("R"+str(i)))
    exec("result.append(%s)" % ("R"+str(i)))
```

This part of the program save the multiple combination in the "li" variable  
And create the empty array "result" for store the result and fill with 0 for the multiplication using numpy module

```python
for B in li:
    result = np.dot(A, list(B))
    ZeroChecker = [item for item,
                   count in collections.Counter(result).items() if count > 1]

    if (n % 2) == 0:
        if sum(result) == 0 and 0 not in result:
            print("A x "+str(B)+" => "+str(result))
    else:
        if sum(result) == 0 and 0 in result and 0 not in ZeroChecker:
            print("A x "+str(B)+" => "+str(result))

```

This part of the program multiply the A matix with the resulted combinational matrixes

I used some filters for the desired output you expected and show the result wit the Combinational matrix too

```python
for B in li:
    result = np.dot(A, list(B))
    ZeroChecker = [item for item,
                   count in collections.Counter(result).items() if count > 1]

    if (n % 2) == 0:
        if sum(result) == 0 and 0 not in result:
            print(result)
    else:
        if sum(result) == 0 and 0 in result and 0 not in ZeroChecker:
            print(result)

```

If you want the desired outp only you can replace this code
