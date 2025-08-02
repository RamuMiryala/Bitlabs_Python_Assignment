# classroom_performance.py

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_average(self):
        return round(sum(self.marks) / len(self.marks), 2) if self.marks else 0.0


def calculate_all_averages(students_dict):
    """
    Calculates average marks for each student.

    Parameters:
    students_dict (dict): Dictionary of student names and their list of marks.

    Returns:
    dict: Dictionary with student names and their average marks.
    """
    averages = {}
    for name, marks in students_dict.items():
        student = Student(name, marks)
        averages[name] = student.calculate_average()
    return averages


def find_top_performer(average_dict):
    """
    Finds the student with the highest average marks.

    Parameters:
    average_dict (dict): Dictionary with student names and their average marks.

    Returns:
    str: Name of the top performer.
    """
    return max(average_dict, key=average_dict.get)


def main():
    students = {
        "John": [85, 78, 92],
        "Alice": [88, 79, 95],
        "Bob": [70, 75, 80]
    }

    average_marks = calculate_all_averages(students)
    print("Average Marks:", average_marks)

    top_student = find_top_performer(average_marks)
    print("Top Performer:", top_student)


if __name__ == "__main__":
    main()
