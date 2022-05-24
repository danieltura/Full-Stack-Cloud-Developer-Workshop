class Student:
    def __init__(self, first_name, last_name, grade, program, student_number):
        self.first_name = first_name
        self.last_name = last_name
        self.student_number = student_number
        self.program = program
        self.grade = grade


class StudentRecords:
    def __init__(self):
        self.students = {}

    def add(self, student: Student):
        if student.student_number not in self.students:
            self.students[student.student_number] = student

    def update(self, student: Student):
        if student.student_number in self.students:
            self.students[student.student_number] = student

    def search(self, student_number):
        if student_number in self.students:
            return self.students[student_number]

    def delete(self, student_number):
        if student_number in self.students:
            del self.students[student_number]

    def get_all_students(self):
        return self.students
