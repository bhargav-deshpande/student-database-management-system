from database import create_table
from operation import(
    op_add_student,
    op_viw_all,
    op_search_student,
    op_update_student,
    op_student_delete,
    op_view_average,
    op_view_sorted
)

def menu():
    print("\n"+"="*40)
    print("Student Database Management System")
    print("="*40)
    print("1.Add Student")
    print("2.View Students")
    print("3.Search Student")
    print("4.Update Student")
    print("5.Delete Student")
    print("6.Average of data")
    print("7.Sorted list of Students according to marks")
    print("8.Exit")
    print("="*40)

def main():
    create_table()
    while True:
        menu()
        choice=int(input("Enter your choice:"))
        match choice:
            case 1: op_add_student()
            case 2: op_viw_all()
            case 3: op_search_student()
            case 4: op_update_student()
            case 5: op_student_delete()
            case 6: op_view_average()
            case 7: op_view_sorted()
            case 8:
                print("Exit")
                break
            case _:
                print("Invalid Input")

if __name__=="__main__":
    try:
        main()
    except ValueError:
        print("Keyboard Interrupted")