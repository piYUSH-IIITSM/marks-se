from dataclasses import dataclass, field

@dataclass
class Student:
    name: str
    marks: int | None = None


@dataclass
class MarksSystem:
    students: dict = field(default_factory=dict)

    def add_student(self, roll_no: str, name: str):
        if roll_no in self.students:
            raise ValueError("Student already exists")
        self.students[roll_no] = Student(name=name)

    def add_marks(self, roll_no: str, marks: int):
        if roll_no not in self.students:
            raise ValueError("Student not found")
        self.students[roll_no].marks = marks
