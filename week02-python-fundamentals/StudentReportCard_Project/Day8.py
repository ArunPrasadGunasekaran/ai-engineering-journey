import json
import add_student
#Get input from user
student_name=input("Please enter student name: ")
student_id=input("Please enter student ID: ")
student_maths_mark=int(input("Please enter student maths mark: "))
student_science_mark=int(input("Please enter student science mark: "))
student_english_mark=int(input("Please enter student english mark: "))

new_student_reportCard=(add_student.studentReportCard(student_name,student_id,student_maths_mark,student_science_mark,student_english_mark))

try:                                                  #exception handling
    with open("OurStudent_report.json",'r') as file:
        file_exist= json.load(file)
        print(f'Already available:{file_exist}')      #opening json file and checking whether the file is available if the file is available
                                                      # , it will proceed further if not it will move to the exception handler flow
        for i in file_exist:                          # for loop and if condition is used to find is the student id is already available
                                                      # , if available it will replace the existing one else it will add a new one
            if i==student_id:
                file_exist[i]=new_student_reportCard
            else:
                file_exist.update(new_student_reportCard)
        with open("OurStudent_report.json", 'w') as file:
            json.dump(file_exist, file, indent=4)
            print(f'UpdatedRecords:{file_exist}')
except FileNotFoundError:
    print("file not found so creating a new one")
    with open("OurStudent_report.json", 'w') as file:
        json.dump(new_student_reportCard, file, indent=4)




