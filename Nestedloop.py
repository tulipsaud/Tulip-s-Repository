lower = int(input("enter lower range:"))
upper = int(input("enter upper range:"))
print("Prime numbers beteen", lower, "and", upper, "are :")
for num in range(lower, upper +1 ):
    if num > 1:
        for i in range(2, num):
            if (num% i) == 0:
                break 
        else:
            print (num)
string = input("Enter your word:")
char = input("please enter your character as well:")
i = 0
count = 0
while(i < len(string)):
 if(string[i] == char):
     count = count + 1
 i = i + 1 
print("\nThe Total number of time", char, "has occured = ", count)
num = int(input("Enter no:"))
t = num 
numLen = 0
while t>0:
    numLen = numLen+1
    t = int(t/10)
if numLen>=4:
 numLen = int(numLen/2)
 chk = 0 
 while num>0: 
    rem = num%10
    if chk==numLen:
        mid = rem 
    elif chk == (numLen-1):
        midtwo = rem 
    num = int(num/10)
    chk = chk+1
 prod = mid*midtwo
 print("Product of mid digits(" + str(mid)+ "*" +str(midtwo)+") = ", prod)
else: 
 print("its not 4 or more")

