a = input("Enter a word:")
for i in a:
    if (i == "A"):
        print("A found")
        break
    else:
        print("A not found")
for x in range(10,21):
    if x % 20 == 0:
        print("twist")
    elif x % 15 == 0:
        pass
    elif x % 10 == 0:
        print("fizz")
    elif x % 5 == 0:
        print("buzz")
    else:
        print(x)
var = 10
while var > 0:
    var = var - 1
    if var == 6:
        continue
    print("Current variable value:", var)
print("\nGoodbye")
for i in range(25):
    if i % 10==0:
        print(i)
        continue
    print ("value is:", i)
    