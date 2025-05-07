print("Creating a half Triangle:")
n = int(input("EnTer your number of rows:"))
for i in range(n):
    for j in range(i+1):
        print("*", end =" ")
    print ()
rowSize = int(input("enter number of rows:"))
if rowSize%2==0:
    halfDiamRow = int(rowSize/2)
else: 
    halfDiamRow = int(rowSize/2)+ 1
space = halfDiamRow-1
for i in range(1, halfDiamRow+1):
    for j in range(1, space+1):
        print(end=" ")
    space = space - 1
    num = 1
    for j in range(2*i-1):
        print(end=str(num))
        num = num+1
    print()
space = 1
for i in range(1, halfDiamRow):
    for j in range(1, space+1):
     print(end=" ")
    space = space +1 
    num = 1
    for j in range(1, 2*(halfDiamRow-i)):
        print (end=str(num))
        num = num+1
    print()
n = int(input("Enter number of rows:"))
num = 1
for i in range(n):
    for j in range(i+1):
        print(num, end =" ")
        num = num + 1
    print ()