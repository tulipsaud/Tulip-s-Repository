a = 5
b = 10
c = 0
if a and b and c:
    print("all boolean value as true")
else:
    print("atleast one boolean value is false")
a = 5
b = -5
c = -10
if a > 0 or b > 0:
    print("either is greater than 0")
else:
    print("none is greater than 0")
if b > 0 or c > 0:
    print("either is greather than 0")
else:
    print("none is greather than 0")
a = 10
b = 15
c = 20
print(a != b)
print(b != c)
a = 10
b = 5
if (a == 1) != (b == 5):
 print("yes")
a = int(input("Enter your number:"))
if a%2 != 0:
    print("not even number")
height = float(input("Enter Height"))
weight = float(input("Enter Weight"))
BMI = weight / (height/100)**2
print("BMI..", BMI)
if BMI <= 18:
 print("u r underweight.")
elif BMI <= 25:
 print("u r healthy")
elif BMI <= 30:
 print("u r overweight.")
elif BMI <= 35:
 print (" ur r severely overweight.")
elif BMI <= 40:
 print("u r obese")
else:
   print(" u r severely obese.") 