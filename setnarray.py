my_set = {1, 2, 3}
print(my_set)
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)
my_set = {1, 2, 3, 4, 3, 2}
print(my_set)
my_set = set([1, 2, 3, 2])
print(my_set, "\n")
num_set = set([0, 1, 3, 4, 5])
print("Original set:", num_set) 
num_set.pop()
print("After removing the first element from the said set:", num_set)

setx = {"apple", "banana"}
sety = {"banana", "papaya"}
print("Original set elements:")
print(setx)
print(sety)
print("Union of two said sets:")
setz = setx.union(sety)
print(setz)

import array as arr
array_num = arr.array('i', [1, 4, 4, 6, 7, 9, 4])
print("Original array: ", (array_num))
print("Number of occurrences of the number 4 in the said array: " + str(array_num.count(4)))
array_num.reverse()
print("Reverse the order of the items:")
print(str(array_num))

set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7, 9}
symmetric_diff = set_A.symmetric_difference(set_B)
print("Symmetric Difference (A and B):", symmetric_diff)
diff_A_B = set_A.difference(set_B)
print("Difference (A - B):", diff_A_B)






