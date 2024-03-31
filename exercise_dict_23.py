student_marks={
    "Ajas":92,
    "Bheem":81,
    "Raju":56,
    "Khalia":78
}
student_marks["Raju"]=71
for i in student_marks:
    if student_marks[i]>=91 and student_marks[i]<=100:
        student_marks[i]="A+"
    elif student_marks[i]>=81 and student_marks[i]<=90:
        student_marks[i]="A"
    elif student_marks[i]>=71 and student_marks[i]<=80:
        student_marks[i]="B+"
    elif student_marks[i]>=61 and student_marks[i]<=70:
        student_marks[i]="B"
    elif student_marks[i]>=51 and student_marks[i]<=60:
        student_marks[i]="C"
    elif student_marks[i]>=41 and student_marks[i]<=50:
        student_marks[i]="D"
    else:
        student_marks[i]="F"
print(student_marks)
