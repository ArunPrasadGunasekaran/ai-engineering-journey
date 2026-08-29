
def studentReportCard(student_name,student_id,student_maths_mark,student_science_mark,student_english_mark):
    studentreport = {}
    studentreport[student_id] = {
            "name":student_name,
            "marks":
            {
                "maths" : student_maths_mark ,
                "science" : student_science_mark ,
                 "english" :  student_english_mark
            },
            "total":student_maths_mark+student_science_mark+student_english_mark
        }
    return studentreport
