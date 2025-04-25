medical_cause = input ("any medical reason Y or N:")
atten = int(input("enter the attendance of the student:"))
if medical_cause == 'Y': 
    print("Allowed")
else:
    if atten>80:
        print("Allowed")
    else:
        print("Not Allowed")
units = int(input("Enter Number of Units Consumed"))
if (units < 50):
    amount = units * 2.6
    surcharge = 25
elif(units<= 100):
    amount = 130 + ((units - 65) * 3.25)
    surcharge = 25
elif (units <= 200):
    amount = 130 + 162.5 + ((units - 100) * 5.26)
    surcharge = 45
else: 
    amount = 130 +162.50 + 526 + ((units - 200) * 8.45)
    surcharge = 75
total = amount + surcharge 
print("\nBill = %.2f" %total)
