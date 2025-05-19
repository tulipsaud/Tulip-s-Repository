try :
 number = int(input("Enter a number:"))
 print("The number entered is:", number)
except ValueError as er:
 print("Exception:", er)
try:
 num1, num2 = eval(input("Enter 2 numbers, seperated by a comma:"))
 result = num1 / num2
 print("The result is:", result)
except ZeroDivisionError:
 print("Division by zerio is error")
except SyntaxError:
 print("Comma is missing")
except:
 print("Invalid input")
else:
 print("No exceptions")
finally:
 print("This will execute no matter what")
valid = False
while not valid:
 try:
  n=int(input("Enter a number:"))
  while n%2==0:
   print ("bye")
  valid = True
 except ValueError:
  print("Inavlid")
def check_age(age):
    try:
        age = int(age)
        if age < 0:
            raise ValueError("Age cannot be negative")
        if age % 2 == 0:
            print("The age", {age} ,"is even.")
        else:
            print("The age", {age} ,"is odd.")
    except ValueError as er:
        print(f"Inavlid age entered")
user_input = input("Enter age:")
check_age(user_input)