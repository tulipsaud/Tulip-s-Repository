num1 = [3, 4, 5]
num2 = [6, 7, 8]
result = map(lambda x, y: x + y, num1, num2)
print("Adding the lists")
print(list(result))
nums = [1,2,3,4]
def sq(n):
    return n*n
square = list(map(sq,nums))
print("Square of numbers in list")
print(square)

s1 = (2, 3, 1)
s2 = ('b', 'a', 'c')
s3 = list(zip(s1, s2))
print(s3, "\n")
list1 = [10, 20, 30, 40]
list2 = [200, 2000, 300, 3000]
for x, y in zip(list1, list2[::-1]):
    print(x, y)
stocks = ['reliance', 'infosys', 'tcs']
prices = [2175, 1819, 2750]
new_dict = {stocks: prices for stocks, prices in zip(stocks, prices)}
print('\n{}'.format(new_dict))

for i in range(20):
    if i == 10:
        print(exit)
        exit()
    print(i)
