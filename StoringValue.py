apple1 = 52
apple2 = 40
apple3 = 71
apple4 = 23
apple5 = 19
sum = apple1+apple2+apple3+apple4+apple5
print("the sum of all the 5 apples is..", sum)
average = sum/5
print("the average of all the tree is:", average) 
Amount = int(input("Enter the amount to withrdaw"))
note_1 = Amount//100
note_2 =(Amount%100)//50
note_3 = ((Amount%100)%50)//10 
print("notes of 100 rupee", note_1)
print("notes of 50 rupee", note_2)
print("notes of 10 rupee", note_3)
print("Enter Marks of Each")
math = int(input("maths :"))
english = int(input("english :"))
science = int(input("science:"))
nepali = int(input("nepali :"))
sum = math+english+science+nepali
print("sum of these subjects", sum)
print("Converting to Percentage")
perc = (sum/400)*100
print(end="Percentage Mark =")
print(perc)
