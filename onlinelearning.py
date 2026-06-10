"""Problem Statement
An online learning platform provides different fees for basic and advanced courses.
Create a class Course with a method course_fee() that displays:
Course Fee: ₹5000
Create a child class AdvancedCourse that overrides the method and displays:
Course Fee: ₹12000
Display the fee of an advanced course.
Test Case 1
Input:Advanced Course
Output
Course Fee: ₹12000
Test Case 2
Input:Basic Course
Output:Course Fee: ₹5000"""

class Course:
    def course_fee(self):
        print("Course Fee: Rs.5000")
class AdvancedCourse(Course):
    def course_fee(self):
        print("Course Fee: Rs.12000")
course=AdvancedCourse()
course.course_fee()
course=Course()
course.course_fee()