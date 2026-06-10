class Employee:
    def __init__(self):
        print("Employee works 8 hours a day")
class Intern(Employee):
    def work_hours(self):
        print("Intern works 8 hours a day")
intern=Intern()
intern.work_hours()