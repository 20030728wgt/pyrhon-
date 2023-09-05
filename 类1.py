


class Student:

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {"语文": 0, "数学": 0}

    def set_grade(self, course, grade):
        if course in self.grades:
            self.grades[course] = grade

    def print_grades(self):
        print(f"学生{self.name}(学号:{self.student_id})的成绩：")
        for course in self.grades:
            print(f"{course}:{self.grades[course]}分数")


zeng = Student("小曾", "10086")
zeng.set_grade("数学", 95)
zeng.set_grade("语文", 88)
zeng.print_grades()
print(zeng.grades)













