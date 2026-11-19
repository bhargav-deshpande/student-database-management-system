from database import(
    add_student,
    get_all_students,
    get_student_by_roll_no,
    update_student,
    delete_student,
    get_average_marks,
    get_students_sorted_by_marks
)

def display_students_from_table(students):
    if not students:
        print("\nDatabase is Empty!")
        return
    print("\n"+"="*65)
    print(f"{'Roll No':<10}{'Name':<20}{'Age':<8}{'Course':<15}{'Marks':<8}")
    print("-"*65)
    for s in students:
        print(f"{s[0]:<10}{s[1]:<20}{s[2]:<8}{s[3]:<15}{s[4]:<8}")
    print("="*65)

def op_add_student():
    try:
        roll_no=int(input("Enter Roll No:"))
        if get_student_by_roll_no(roll_no):
            print("Roll No already exists in record")
            return
        name=input("Enter Name:").strip()
        if not name:
            print("Name cannot be empty")
            return
        age=int(input("Enter Age:"))
        if age<=0:
            print("Age must be positive")
            return
        course=input("Enter Course:").strip()
        if not course:
            print("Course cannot be empty")
            return
        marks=int(input("Enter marks:"))
        if marks<0 or marks>100:
            print("Marks must be between 0 and 100")
            return
        add_student(roll_no,name,age,course,marks)
        print("Student added successfully")
    except ValueError:
        print("Invalid Inputs given")

def op_viw_all():
    records=get_all_students()
    display_students_from_table(records)

def op_search_student():
    try:
        roll_no=int(input("Enter Roll No to find:"))
        records=get_student_by_roll_no(roll_no)
        if records:
            display_students_from_table([records])
        else:
            print("No Student found")
    except ValueError:
        print("Invalid Input given")

def op_update_student():
    try:
        roll_no=int(input("Enter Roll number of Student that needs to be updated"))
        student=get_student_by_roll_no(roll_no)
        if not student:
            print("NO Student found with this Roll No")
            return
        print("Current Details:")
        print(f"Name:{student[1]},Age:{student[2]},Course:{student[3]},Marks:{student[4]}")
        name=input("Enter name:").strip() or student[1]
        age_st=input("Enter age:").strip()
        age=int(age_st) if age_st else student[2]
        course=input("Enter course:").strip() or student[3]
        marks_st=input("Enter marks:").strip()
        marks=int(marks_st) if marks_st else student[4]
        update_student(roll_no,name,age,course,marks)
        print("Record Updated Successfully")
    except ValueError:
        print("Invalid Input")

def op_student_delete():
    try:
        roll_no=int(input("Enter Roll No to delete"))
        student=get_student_by_roll_no(roll_no)
        if not student:
            print("Student not found")
            return
        delete_student(roll_no)
        print("Student data deleted")
    except ValueError:
        print("Invalid Input")

def op_view_average():
    result=get_average_marks()
    print('Average Marks of Students are: ',result)

def op_view_sorted():
    student=get_students_sorted_by_marks()
    display_students_from_table(student)