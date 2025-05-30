empty_list = []
print(empty_list)
numbers = [1, 2, 3, 4, 5]
print(numbers)
triples = [8, 9, 10] * 3
print(triples)
aList = [200, 1200, 12000, 24000, 2000]
aList = aList[::-1]
print(aList, "\n")
def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
             ctr += 1
             lst.append(word)
    print("List of words with first and last character same:\n", lst)
    return ctr
count = match_words(['def', 'lol', 'lmk', '505', 'no'])
print("Number of words having first and last character same:", count)

L = [5, 10, 15, 20, 25]
print("Original list :", L)
count = 0
for i in L:
    count += i
avg = count / len(L)
print("sum =", count)
print("average =", avg)
L.sort()
print("Smallest element is:", L[0])
print("Largest element is:", L[-1])

s1 = [2, 3, 1]
s2 = ['b', 'a', 'c']
s3 = list(zip(s1, s2))
print(s3, "\n")
list1 = [10, 100, 1000, 10000]
list2 = [100, 200, 300, 400]
for x, y in zip(list1, list2[::-1]):
    print(x, y)