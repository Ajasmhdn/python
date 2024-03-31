# #nested dictionaries
# student_data={
#     "Ajas":{
#         "marks":92,
#         "grade":"A+"
#     },
#     "Bheem":{
#         "marks":81,
#         "grade":"A"
#     },
#     "Raju":{
#         "marks":56,
#         "grade":"C"
#     },
#     "Khalia":{
#         "marks":78,
#         "grade":"B+"
#     }
# }
# # print(student_data["Ajas"])
# # print(student_data["Ajas"]["marks"])
# # print(student_data["Ajas"]["grade"])

# student_data["Ajas"]["marks"] = 99
# del student_data["Ajas"]["marks"]
# student_data["Ajas"]["awards"] = 'Best Student'
# print(student_data["Ajas"])


#nesting list in dictionaries

# travel={
#     "kerala":["Munnar","Thekkady","Kochi"],
#     "karnataka":["Bangalore","Mysore","Hampi"],
#     "tamilnadu":["Madur","Chennai","Ooty"]
# }
# print(travel["karnataka"])

student_data=[
    {   "name":"Ajas",
        "marks":92,
        "grade":"A+"
    },
    {   "name":"Bheem",
        "marks":81,
        "grade":"A"
    },
    {   "name":"Raju",
        "marks":56,
        "grade":"C"
    },
    {   "name":"Khalia",
        "marks":78,
        "grade":"B+"
    }
]
print(student_data)