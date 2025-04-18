x = 100
if (type(x) is int):
    print("true")
else:
    print("false")
y = 0.1
if (type(x) is float):
    print("true")
else:
    print("false")
a = 30
b = 30
if ( x is y):
    print("same value")
y = 300
if (x is not y):
    print("different value")
a = 10
b = -10
print("a >> 1 =", a >> 1)
print("b >> 1 =", b >> 1)
a = 5
b = -10
print("a << 1 =", a >> 1)
print("b << 1 =", b << 1)
print("Enter Marks of the 5 subjects")
maths = int(input())
english = int(input())
history = int(input())
science = int(input())
social = int(input())
tot = maths+english+history+science+social
avg = tot/5
if avg>=85 and avg<=100:
 print("Grade is A")
elif avg>=70 and avg<=85:
    print("Grade is B")
elif avg>=55 and avg<=70:
 print("Grade is C")
elif avg>=40 and avg<=55:
   print("Grade is D")
else: 
   print("Grade is F")
