from batch import Batch
from student import Student

class DemoDB:

    def __init__(self):
        self.__batches = []

    def existing_records(self):
        batch1 = Batch()
        # batch1 1 info
        batch1.b_id = 1001
        batch1.b_name = "RIT AI - AP"
        # course info
        batch1.course.c_id = 101
        batch1.course.c_name = "AI - AP"
        batch1.course.credits = 5
        # teacher info 
        batch1.teacher.p_id = 11
        batch1.teacher.name = "Bilal"
        batch1.teacher.cnic = "33103-1234567-1"
        batch1.teacher.fullAddress.city = "Fsd"
        batch1.teacher.fullAddress.country = "Pak"
        batch1.teacher.salary = 20000
        # student info 1
        student1 = Student()
        student1.p_id = 1
        student1.name = "Anas"
        student1.cnic = "33103-1234567-9"
        student1.fullAddress.city = "Lhr"
        student1.fullAddress.country = "Pak"
        student1.cgpa = 3.8
        student1.fee = 40000
        batch1.students.append(student1)  
        # student info 2
        student2 = Student()
        student2.p_id = 2
        student2.name = "Ahmad"
        student2.cnic = "33103-1234567-8"
        student2.fullAddress.city = "Isd"
        student2.fullAddress.country = "Pak"
        student2.cgpa = 3.7
        student2.fee = 30000
        batch1.students.append(student2)
        
        self.__batches.append(batch1)   # add 1st batch 

        # batch2 = Batch()
        # add batch 2 info ... code here 

    def display_all_records(self):
        records = ''
        batches_len = len(self.__batches)
        for i in range(batches_len):
            records += '** Batach Info ** \n'
            records += f'Batch Id: {self.__batches[i].b_id} \n'
            records += f'Batch Name: {self.__batches[i].b_name} \n'

            records += '** Course Info ** \n'
            records += f'Couerse Id: {self.__batches[i].course.c_id} \n'
            records += f'Couerse Name: {self.__batches[i].course.c_name} \n'
            records += f'Couerse Credits: {self.__batches[i].course.credits} \n'
            
            records += '** Teacher Info ** \n'
            records += f'Teacher Id: {self.__batches[i].teacher.p_id} \n'
            records += f'Teacher Name: {self.__batches[i].teacher.name} \n'
            records += f'Teacher CNIC: {self.__batches[i].teacher.cnic} \n'
            records += f'Teacher City: {self.__batches[i].teacher.fullAddress.city} \n'
            records += f'Teacher Country: {self.__batches[i].teacher.fullAddress.country} \n'
            records += f'Teacher Salary: {self.__batches[i].teacher.salary} \n'

            records += '** Student Info ** \n'
            for j in range(len(self.__batches[i].students)):
                records += f'Student Id: {self.__batches[i].students[j].p_id} \n'
                records += f'Student Name: {self.__batches[i].students[j].name} \n'
                records += f'Student CNIC: {self.__batches[i].students[j].cnic} \n'
                records += f'Student City: {self.__batches[i].students[j].fullAddress.city} \n'
                records += f'Student Country: {self.__batches[i].students[j].fullAddress.country} \n'
                records += f'Student CGPA: {self.__batches[i].students[j].cgpa} \n'
                records += f'Student Fee: {self.__batches[i].students[j].fee} \n'

        return records

    def add_new_batch(self, new_batch):
        self.__batches.append(new_batch)

    def search_student_record(self, search_name):
        records = ''
        batches_len = len(self.__batches)
        for i in range(batches_len):
            for j in range(len(self.__batches[i].students)):
                if self.__batches[i].students[j].name.lower() == search_name.lower():
                    records += f'Batch Name: {self.__batches[i].b_name} \n'
                    records += f'Couerse Name: {self.__batches[i].course.c_name} \n'
                    records += f'Teacher Name: {self.__batches[i].teacher.name} \n'

                    records += f'Student Id: {self.__batches[i].students[j].p_id} \n'
                    records += f'Student Name: {self.__batches[i].students[j].name} \n'
                    records += f'Student CGPA: {self.__batches[i].students[j].cgpa} \n'

        return records
