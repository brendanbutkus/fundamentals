# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# Change the last_name of the first student from 'Jordan' to 'Bryant'
# In the sports_directory, change 'Messi' to 'Andres'
# Change the value 20 in z to 30

# x = [[5, 2, 3], [10, 8, 9]]
# students = [
#     {'first_name':  'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'}
# ]

# x[1][0] = 15
# print(x)

# students[0]['last_name'] = 'Bryant'
# print(students)

# sports_directory = {
#     'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer': ['Messi', 'Ronaldo', 'Rooney']
# }
# sports_directory['soccer'][0] = 'Andres'
# print(sports_directory['soccer'])

# z = [{'x': 10, 'y': 20}]
# z[0]['y'] = 30
# print(z)


# students = [
#     {'first_name':  'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'},
#     {'first_name': 'Mark', 'last_name': 'Guillen'},
#     {'first_name': 'KB', 'last_name': 'Tonel'}
# ]

# # to iterate throught the dictionary, i want to use a forward loop..then I want to specifically print each key and it's corresponding value on the same line
# def iterateDictionary(dict):
#     for i in range(0,len(dict)):
#         # the range ends at len(dict) because it will halt the value right before the end of the range..making it 0 -3 and then stopping at four
#         newBox = ''
#         for key, val in dict[i].items():
#             newBox += (f'{key} - {val}')
#             # the items method is for dictionaries, because it is able to identify the individual keys and their corresponding values
#             print(newBox)
# iterateDictionary(students)


# allStars = [
#         {'firstName':  'Magic', 'lastName': 'Johnson'},
#         {'firstName': 'Scottie', 'lastName': 'Pippen'},
#         {'firstName': 'Clyde', 'lastName': 'Drexler'},
#         {'firstName': 'Dennis', 'lastName': 'Rodman'}
# ]
# def iterateDictionary2(key_name, some_list):
#     for i in range(0, len(some_list)):
#         # newLine = ""
#         for key, val in some_list[i].items():
#             if key == key_name:
#                 print(val)
# iterateDictionary2('firstName', allStars)



# # PROBLEM 4 BELOW



# # Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for i in range(0, len(some_dict)):
        for key, val in some_dict.items():
            print(f"{len(val)} {key}")
            for i in range(0, len(val)):
                    print(val[i])




printInfo(dojo)


# def print_info(dict):
#     for key,val in dict.items():
#         print("--------------")
#         print(f"{len(val)} {key.upper()}")
#         for i in range(0, len(val)):
#             print(val[i])

# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
