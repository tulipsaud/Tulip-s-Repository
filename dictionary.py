test_dict = {'apple' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'health' : 1}
print("The original dictionary : " + str(test_dict))
k = 2
res = 0
for key in test_dict:
    if test_dict[key] == k:
        res = res + 1
print("Frequency of K is : " + str(res))

student_data = {'id1': 
    { 'name': ['James'],
        'class': ['V'],
        'subject_integration': ['english, math, science'] 
    },
    'id2': 
    {'name': ['Surya'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id3': 
    {'name': ['Rudra'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id4': 
    { 'name': ['Surya'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
}
result = {}
for key,value in student_data.items():
    if value not in result.values():
        result[key] = value
print (result)

country_code = {
    'India': '0091',
    'Australia': '0025',
    'Nepal': '00977'}
print("Country code for India -")
print(country_code.get('India', 'Not Found'))
print("Country code for Turkey -")
print(country_code.get('Turkey', 'Not Found'))



