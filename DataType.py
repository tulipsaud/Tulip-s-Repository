name = "tulip"
age = 15
is_student = True
weight = 54.5
print("Name:", name)
print("data type of name is:", type (name))
print("age:", age)
print("data type of age is:", type (age))
print("is_student:", is_student)
print("data type of is_student is:", type(is_student))
print("Weight:", weight)
print("data type of weight:", type (weight))
print("\n After type casting weight...")
weight = int(weight)
print(weight)
print("data type of weight is:", type (weight))
x = 10
y = 20
print("\nAddition of the two numbers is", x+y)
x = str(x)
y = str(y)
print("\nAddition of x and y", x+y)
text = str(input("Enter a string:"))
revText = text [::-1]
text = revText
print("Revert Text is..")
print(text)
