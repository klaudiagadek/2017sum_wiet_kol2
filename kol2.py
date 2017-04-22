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
import json
import numpy as np
from optparse import OptionParser
import io

try:
    to_unicode = unicode
except NameError:
    to_unicode = str
from shutil import copyfile


class Diary(object):
    def __init__(self, path_to_file):
        self.students_list = []
        self.attendance_of_student = {}
        self.students_scores = {}
        self.subjects = []
        self.data_loaded = {}
        self.diary_file = path_to_file
        self.load_data_from_diary(self.diary_file)

    def load_data_from_diary(self, data_file):
        with open(data_file) as data_file:
            self.data_loaded = json.load(data_file)
        self.subjects = self.data_loaded["subjects"]
        for student in self.data_loaded["children"]:
            self.attendance_of_student[student["name"]] = student["attendance"]
            self.students_list.append(student["name"])
            for subject in self.subjects:
                self.students_scores[student["name"], subject] = student[subject]

    def get_students_average_attendance(self):
        attendance_mean = np.mean(self.attendance_of_student.values())
        return attendance_mean

    def get_student_subject_average_score(self, student_name, subject):
        if self.students_scores[student_name, subject]:
            subject_average_score = np.mean(self.students_scores[student_name, subject])
            return subject_average_score
        else:
            raise Exception("No scores")

    def get_student_total_average_score(self, student_name):
        scores = []
        [scores.extend(self.students_scores[student_name, subject]) for subject in self.subjects]
        average_score = np.mean(scores)
        return average_score

    def get_students_average_score_in_class(self):
        scores = []
        [[scores.extend(self.students_scores[student_name, subject]) for subject in self.subjects] for student_name in
         self.students_list]
        average_class_score = np.mean(scores)
        return average_class_score

    def print_info_about_students(self):
        print "Students list {}".format(self.students_list)
        print "Students average score {}".format(self.get_students_average_score_in_class())
        print "Students average attendance {}".format(self.get_students_average_attendance())

    def print_info_about_student(self, student):
        try:
            print "Student: {} has total average score {} ".format(student,
                                                                   self.get_student_total_average_score(student))
        except KeyError:
            print "Student doesn't exist"

    def print_info_about_student_subject(self, student, subject):
        try:
            print "Student: {} has average score {} {} subject".format(student,
                                                                       self.get_student_subject_average_score(student,
                                                                                                              subject),
                                                                       subject)
        except KeyError:
            print "Wrong values subject or student doesn't exist"
        except Exception:
            print "{} has no {} scores".format(student, subject)

    def add_student(self):
        try:
            student_name = raw_input("Give me name and surname")
            attendance = int(raw_input("Attendance"))
            print "Add scores"
            scores = {}
            for subject in self.subjects:
                scores[subject] = raw_input(subject)
                scores[subject] = [int(i) for i in scores[subject].split()]
                if not max(scores[subject]) <= 6 and 1 <= min(scores[subject]):
                    break
            student_record = dict(name=student_name, attendance=attendance, Matmematyka=scores["Matmematyka"],
                                  Polski=scores["Polski"], Angielski=scores["Angielski"], Historia=scores["Historia"],
                                  Biologia=scores["Biologia"], Chemia=scores["Chemia"], Fizyka=scores["Fizyka"],
                                  Geografia=scores["Geografia"])
            self.data_loaded["children"].append(student_record)
            copyfile(self.diary_file, "diary_copy.json")
            with io.open(self.diary_file, 'w', encoding='utf8') as outfile:
                str_ = json.dumps(self.data_loaded,
                                  indent=4, sort_keys=True,
                                  separators=(',', ': '), ensure_ascii=False)
                outfile.write(to_unicode(str_))
        except:
            print "Wrong values!"


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename",
                      help="write report to FILE", metavar="FILE")
    (options, args) = parser.parse_args()

    class_diary = Diary(options.filename)
    class_diary.print_info_about_students()
    class_diary.print_info_about_student_subject("Anna Nowak", "Matmematyka")
    class_diary.print_info_about_student_subject("Anna Nowak", "Historia")
    class_diary.print_info_about_student("Anna Nowak")
    class_diary.print_info_about_student("student")

    input = raw_input("Do you want to add a student? yes/other")
    if input == "yes":
        class_diary.add_student()
