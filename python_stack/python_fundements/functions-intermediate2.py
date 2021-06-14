# x = [ [5,2,3], [10,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]


#1
# x[1][0] = 15
# print(x[1][0]) 

#2
# students[0]["last_name"] = "Bryant"
# print(students[0])

#3
# sports_directory["soccer"][0] = "andres"
# print(sports_directory["soccer"][0])

#4
# print(z[0]["y"]) 
# z[0]["y"] = 30
# print(z[0]["y"]) 

#b

# students = [
#          {'first_name':  'Michael', 'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'},
#          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#          {'first_name' : 'KB', 'last_name' : 'Tonel'} ]

# def iterateDictionary(students):

#     for i in range(len(students)):
#         for key, value in students[i].items():
#             print(f"{key} - {value}", end=",")


#     print(students)
#     return students
# iterateDictionary(students)

#c



# def iterateDictionary2(key, students):
#     for i in range(len(students)):
#         for key, value in students[i].items():
#             if key == "first_name":
#                 print(value)
#     return students
# iterateDictionary2(students[0]["first_name"] , students)

# def iterateDictionary2(key, students):
#     for i in range(len(students)):
#         for key, value in students[i].items():
#             if key == "last_name":
#                 print(value)
#     return students
# iterateDictionary2(students[0]["last_name"] , students)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dict):
    for key in dict:
        print(len(dict[key]), key.upper())
        for value in dict[key]:
            print(value)
       

    return dict
printInfo(dojo)
