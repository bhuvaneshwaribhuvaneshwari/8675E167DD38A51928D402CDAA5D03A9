class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    # Sort the list of student objects based on CGPA in descending order
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Test the function with different input lists of students
if __name__ == "__main__":
    students1 = [
        Student("Alice", "101", 3.8),
        Student("Bob", "102", 3.9),
        Student("Charlie", "103", 3.5),
    ]

    students2 = [
        Student("David", "104", 3.2),
        Student("Eve", "105", 3.7),
        Student("Frank", "106", 3.6),
    ]

    sorted_students1 = sort_students(students1)
    sorted_students2 = sort_students(students2)

    print("Sorted students list 1:")
    for student in sorted_students1:
        print(f"{student.name} (Roll Number: {student.roll_number}) - CGPA: {student.cgpa}")

    print("\nSorted students list 2:")
    for student in sorted_students2:
        print(f"{student.name} (Roll Number: {student.roll_number}) - CGPA: {student.cgpa}")
