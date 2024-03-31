def add_new_student(name,marks,grade):
    student_data.append({
        "name":name,
        "marks":marks,
        "grade":grade
    })



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
add_new_student("Madhav",99,"A+")
print(student_data[4])