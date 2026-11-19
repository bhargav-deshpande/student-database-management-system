import mysql.connector
import os

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_host","localhost"),
        user=os.getenv("DB_user","root"),
        password=os.getenv("DB_password","Your_password"),
        database=os.getenv("DB_name","students_db")
    )

def create_table():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Students(
            roll_no INT PRIMARY KEY,
            name TEXT NOT NULL,
            age INT NOT NULL, 
            course TEXT NOT NULL,
            marks INT NOT NULL
    )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def add_student(roll_no,s_name,age,course,marks):
    conn=get_connection()
    cursor=conn.cursor()
    query="""
    INSERT INTO Students(roll_no,s_name,age,course,marks)
    VALUES (%s,%s,%s,%s,%s)
    """
    cursor.execute(query,(roll_no,s_name,age,course,marks))
    conn.commit()
    cursor.close()
    conn.close()

def get_all_students():
    conn=get_connection()
    cursor=conn.cursor()
    query="SELECT * FROM Students"
    cursor.execute(query)
    records=cursor.fetchall()
    cursor.close()
    conn.close()
    return records

def get_student_by_roll_no(roll_no):
    conn=get_connection()
    cursor=conn.cursor()
    query="SELECT * FROM Students WHERE roll_no=%s"
    cursor.execute(query,(roll_no,))
    by_roll_no=cursor.fetchone()
    cursor.close()
    conn.close()
    return by_roll_no

def update_student(roll_no,s_name,age,course,marks):
    conn=get_connection()
    cursor=conn.cursor()
    query="""
    UPDATE Students SET s_name=%s,age=%s,course=%s,marks=%s
    WHERE roll_no=%s
    """
    cursor.execute(query,(s_name,age,course,marks,roll_no))
    conn.commit()
    cursor.close()
    conn.close()

def delete_student(roll_no):
    conn=get_connection()
    cursor=conn.cursor()
    query="DELETE FROM Students WHERE roll_no=%s"
    cursor.execute(query,(roll_no,))
    conn.commit()
    cursor.close()
    conn.close()

def get_average_marks():
    conn=get_connection()
    cursor=conn.cursor()
    query="SELECT AVG(marks) FROM Students"
    cursor.execute(query)
    result=cursor.fetchone()
    cursor.close()
    conn.close()
    if result and result[0] is not None:
        return float(result[0])
    return 0.0

def get_students_sorted_by_marks():
    conn=get_connection()
    cursor=conn.cursor()
    query="SELECT * FROM Students ORDER BY marks DESC"
    cursor.execute(query)
    result=cursor.fetchall()
    cursor.close()
    conn.close()
    return result

if __name__=="__main__":
    create_table()
    # add_student(38,"Bhargav",20,"CS",100)
    # records=get_all_students()
    # print("Fetched :",records)