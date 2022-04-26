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
    B = []
    for BPairValue in range(1, round((n/2)+1)):
        B.append(BPairValue)
        B.append(-BPairValue)
else:
    B = [0]
    for BPairValue in range(1, round(n/2)):
        B.append(BPairValue)
        B.append(-BPairValue)
print(A)
print(B)
