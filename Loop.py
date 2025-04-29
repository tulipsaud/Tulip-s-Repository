n = int(input("Enter the number to find sum:"))
sum = 0
for i in range(2, n+2):
    sum = sum+i
    print("\nSum=", sum)
string = input("Please enter string:")
string2 = ('')
for i in string:
    string2 = i + string2
print("n The Original string =", string)
print("And the Reversed string =", string2)
n = int(input("Enter n:"))
print ("numbers from {0} to {1} are:" .format(n,1))
for i in range (n, 0, -1):
    print(i)
    