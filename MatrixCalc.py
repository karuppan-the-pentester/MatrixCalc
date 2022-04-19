n = int(input("Enter the Order Of matrix 'n' : "))

for i in range(1, n+1):
    for j in range(1, n+1):
        Dynamic_Variable_Name = "A"+str(i)+str(j)
        ElementValue = int(input("A"+str(i)+str(j)+" : "))
        exec("%s = %d" % (Dynamic_Variable_Name, ElementValue))
