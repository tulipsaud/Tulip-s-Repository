a = 6
b = 10
c = 20
d = 2
e = 0
e = (b+c) + a / d
print("Value of (b+c) * a / d is", e)
print("Enter a Number (Numerator):")
numn = int(input())
print("Enter a number (Denominator)")
numd = int(input())
if numn%numd==0:
    print("\n" +str(numn)+ "is divisible by" +str(numd))
else:
    print("\n" +str(numn)+ "is not divisible by" +str(numd))
mean1 = 68
wrong_number = 20
correct_number = 48
total_number = 10
sum = mean1 * total_number
print("the sum is:", sum)
num2 = sum -((wrong_number) - (correct_number))
mean2 = num2 / total_number
print("the mean is:", mean2)
a = int(input("enter a value:"))
b = int(input("enter a value 2:"))
c = int(input("enter a value 3:"))
avg = (a + b + c) / 3
print("avg =", avg)
if avg > a and avg > b and avg > c:
    print("%d is higher than %d, %d, %d" %(avg, a , b, c)) 
elif avg > a and avg > b: 
    print("%d is higher than %d, %d" %(avg, a , b)) 
elif avg > b and avg > c:
    print("%d is higher than %d, %d" %(avg, b, c))
elif avg > a and avg > c:
    print("%d is higher than %d, %d" %(avg, a, c))
elif avg > a:
    print ("%d is just higher than %d" %(avg, a))
elif avg > b: 
    print ("%d is just higher than %d" %(avg, b))
elif avg > c:
    print ("%d is just higher than %d" %(avg, c))
else: print("invalid input")
