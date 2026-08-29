import streamlit as st
import json
import markcalculator


with open("week02-python-fundamentals/OurStudent_report.json", "r") as file:
    student=json.load(file)
    print(student)
try :
    studentId = st.text_input("Please enter student id: ")
    button_click = st.button("View Rank Card")
    if button_click:
        if studentId in student:
            st.title("Student Rank Card")
            student_record = student[studentId]
            st.write('Student Id:', (studentId))
            st.write('Name:', (student_record["name"]))
            st.write('Maths_mark:', (student_record["marks"]["maths"]))
            st.write('Science_Mark:', (student_record["marks"]["science"]))
            st.write('English_Mark:', (student_record["marks"]["english"]))
            totalmark=markcalculator.add(student_record["marks"]["maths"],student_record["marks"]["science"],student_record["marks"]["english"])
            st.write('Total Mark:',totalmark)
            average=markcalculator.average(totalmark,len(student))
            st.write('Average:',average )
            st.write('Rank:', markcalculator.rank(average))
        else:
            st.error("student not available")

except ValueError:
    print("Enter valid number")







