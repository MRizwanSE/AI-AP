from demo_db import DemoDB
from batch import Batch
from student import Student

if __name__ == "__main__":
    
    db = DemoDB()

    db.existing_records()

    while True:
        print("Press 1 for Display All Records \nPress 2 for Add New Batch \nPress 3 for Search Student by Name \nPress 4 for Exit : ")
        num = int(input())
        if num == 1:
            print("Display All Records")
            records = db.display_all_records()
            print(records)
        elif num == 2:
            new_batch = Batch()
            # batch info 
            print("Enter Batch Id: ")
            new_batch.b_id = int(input())
            print("Enter Batch Name: ")
            new_batch.b_name = input()
            # course info 
            print("Enter Course Id: ")
            new_batch.course.c_id = input()
            print("Enter Course Name: ")
            new_batch.course.c_name = input()
            print("Enter Course Credits: ")
            new_batch.course.credits = int(input())
            # teacher info
            print("Enter Teacher Id: ")
            new_batch.teacher.p_id = int(input())
            print("Enter Teacher Name: ")
            new_batch.teacher.name = input()
            print("Enter Teacher CNIC: ")
            new_batch.teacher.cnic = input()
            print("Enter Teacher City: ")
            new_batch.teacher.fullAddress.city = input()
            print("Enter Teacher Country: ")
            new_batch.teacher.fullAddress.country = input()
            print("Enter Teacher Salary: ")
            new_batch.teacher.salary = int(input())
            # student info 
            print("Enter Total No. of Students you want to add: ")
            total = int(input())
            for i in range(total):
                new_student = Student()
                print("Enter Student Id: ")
                new_student.p_id = int(input())
                print("Enter Student Name: ")
                new_student.name = input()
                print("Enter Student CNIC : ")
                new_student.cnic = input()
                print("Enter Student City: ")
                new_student.fullAddress.city = input()
                print("Enter Student Country: ")
                new_student.fullAddress.country = input()
                print("Enter Student CGPA: ")
                new_student.cgpa = float(input())
                print("Enter Student Fee: ")
                new_student.fee = int(input())

                new_batch.students.append(new_student)

            db.add_new_batch(new_batch)

        elif num == 3:
            print("Enter Student Name: ")
            std_name = input()
            res = db.search_student_record(std_name)
            print(res)
        elif num == 4:
            print("Good Bye")
            break
        else:
            print("No Action") 
