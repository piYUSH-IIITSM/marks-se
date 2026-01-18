import unittest
from src.app import MarksSystem


class TestSprint1(unittest.TestCase):

    def test_add_student(self):
        ms = MarksSystem()
        ms.add_student("101", "Ravi")
        self.assertIn("101", ms.students)
        self.assertEqual(ms.students["101"].name, "Ravi")

    def test_add_marks(self):
        ms = MarksSystem()
        ms.add_student("102", "Mina")
        ms.add_marks("102", 88)
        self.assertEqual(ms.students["102"].marks, 88)


if __name__ == "__main__":
    unittest.main()
