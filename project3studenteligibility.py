class Student:
    def __init__(self,stu_id,stu_name,attendence):
        self.stu_id=stu_id
        self.stu_name=stu_name
        self.attendence=attendence
class Assessment:
    def __init__(self,assessment_score):
        self.assessment_score=assessment_score
class PlacementManager:
    def __init__(self):
            self.student=[]
    def check_eligibility(self,Assessment):
        if Student.attendence >= 75 and Assessment.assessment_score >= 60:
            return "ELIGIBLE"
        else:
            return "NOT ELIGIBLE"
    def generate_report(self,Student,Assessment):
        print("="*50)
        print("PLACEMENT ELIGIBILITY REPORT")
        print("="*50)
        print(f"\nStudent ID: {Student.stu_id}")
        print(f"Student Name: {Student.stu_name}")
        print("\nAttendance:", str(Student.attendence) + "%")
        print("Assessment Score:", Assessment.assessment_score)
        status = self.check_eligibility(Assessment)
        print("\nPlacement Status:", status)
        print("\n" + "="*50)
student=Student("5101", "Scott",85)
Assessment=Assessment(80)
pm=PlacementManager()
pm.generate_report(student,Assessment)
