import random
class online_Course:
    def __init__(self,course_name,instructor):
        self.course_name = course_name
        self.instructor = instructor
        self.students = []

    def enroll_students(self,student):
        self.students.append(student)
        print(f"{student.name} has been enrolled in the {self.course_name} course.")
    
    def course_details(self):
        print(f"course: {self.course_name} ")
        print(f"Instructor name: {self.instructor}")
        print(f"students enrolled: ")
        for student in self.students:
            print(student.name)

    def completed_course(self,name):
        for student in self.students:
            if name in self.students:
                self.students.remove(student)
                print(f"{name} has completed the course!")
          
        print(f"{name} is not enrolled in this course")

    def avg_grade(self,grades):
        total = sum(student.grades)
        average = total/len(student.grades)
        print(f"Avg. grade in this course is {round(average,1)}")

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades =grades 

course_input = input("Enter a course:").lower()
name =  input("Enter instructor name:").lower()
course= online_Course(course_input,name)

num_students = int(input("Enter number of students: "))
for _ in range(num_students):
    student_name = input("Enter a student name: ").lower()
    grades = []
    for _ in range(3):
        grade = int(input("Enter number of grades: "))
        grades.append(grade)
    student = Student(student_name,grades)
    course.enroll_students(student)
    course.avg_grade(student)

course.course_details()

