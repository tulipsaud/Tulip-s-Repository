num = 10
if num > 0:
    print(num, "is a positive number.")
num = -1
if num < 0:
    print(num, "is a negative number.")
actual_cost = float(input("Enter your Actual Cost:"))
sale_amount = float(input("Enter your Sale Amount:"))
if(sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("Total profit is", amount)
else:
    amount = actual_cost - sale_amount
    print(" No profit and loss is ", amount)
number = int(input("Enter the number:"))
print("Number being checked:", number)
if number%2==0 :
 print("This is an even number.")
else:
 print("This is an odd number.")
temperature = int(input("Enter your temeprature:"))
if temperature<=20 :
 print ("Wear warm clothes, it might be chilly.")
else:
   print ("It's hot, wear shorts.")
