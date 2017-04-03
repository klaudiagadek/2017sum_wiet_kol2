#
# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.
import math


class Diary(object):

    def __init__(self):
        self.students_list = ["Anna Nowak", "Jacek Kowalski"]
        self.attendance_of_student = {"Anna Nowak": 7, "Jacek Kowalski": 9}
        self.students_score = {"Anna Nowak": [3, 4, 5], "Jacek Kowalski": [1, 5, 3]}

    def get_students_total_average_score(self, stundents_name):
        math.average(self.students_score[stundents_name])

    def get_students_total_average_score(self, student_name):
        math.average(self.attendance_of_student[student_name])

    def get_students_average_score_in_class(self):
        math.average(self.students_score.keys())

    def add_student(self, student_name, attendance, scores):
        self.students_list.append(student_name)
        self.attendance_of_student[student_name] = attendance
        self.students_score[student_name] = scores

    def print_students_list(self):
        print "Students list {}".format(self.students_list)

    def print_info_about_student(self, student):
        print "Student: {} has total_average_score {} ".format(student, self.get_students_total_average_score(student))


if __name__ == "__main__":
    class_diary = Diary()
    class_diary.print_students_list()
    input = raw_input("Do you want to add a student? yes/other")
    if input == "yes":
        student_name = raw_input("Give me name and surname")
        attendance = raw_input("Attendance")
        scores = raw_input("Scores")
        scores = [int(i) for i in scores.split()]
        class_diary.add_student(student_name, attendance, scores)
    print class_diary.get_students_average_score_in_class()
