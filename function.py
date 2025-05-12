def well_wishes():
    print("hello")
    print("how are you?")
well_wishes()
def weather_condition():
    print("The weather is pleasant in:", spring)
    print("The weather is same in:", autumn)
spring = "autumn"
autumn = spring
weather_condition()
def add(P,Q):
    return P + Q 
def subtract(P,Q):
    return P - Q
def multiply(P, Q):
    return P * Q
def divide(P, Q):
    return P/Q 
print ("please select:")
print("a: Add")
print("b: Subtract")
print("c: Multiply")
print("d: Divide")
choice = input("Enter ur choice:")
num_1 = int(input("enter first number"))
num_2 = int(input("enter second number"))
if choice == "a":
    print(num_1, "+", num_2, "=", add(num_1, num_2))
elif choice == "b":
    print(num_1, "-", num_2, "=", subtract(num_1, num_2))
elif choice == "c":
    print(num_1, "*", num_2, "=", multiply(num_1, num_2))
elif choice == "d":
    print(num_1, "/", num_2, "=", divide(num_1, num_2))
else: 
   print("Invalid")