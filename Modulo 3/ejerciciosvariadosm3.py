
class Student:
    def _init_(self, name, grades):
        self.name = name
        self.grades = grades

    def get_prom(self):
        return sum(self.grades)/len(self.grades)

# PROBLEMA 1
def enter_students(students_number:int) -> list:
    """[enter students by terminal]

    Args:
        students_number (int): [to range()]

    Returns:
        list: [students list]
    """
    students = list()
    for _ in range(students_number):
        name = input("Enter full name -> ")
        grades = list()
        for number_grade in range(3):
            grade = int(input(f"Enter {(number_grade+1)} grade -> "))
            while grade < 0 or grade > 10:
                grade = int(input(f"Enter {(number_grade+1)} grade -> "))
            grades.append(grade)
        students.append(Student(name, grades))

    return students

# PROBLEMA 2
def get_number_pass_no(students:list) -> tuple:
    """[get number of students pass and no pass]

    Args:
        students (list): [students list]

    Returns:
        tuple: [0 -> student pass, 1 -> no pass]
    """
    number_pass = 0
    number_no_pass = 0
    for student in students:
        if student.get_prom() > 4:
            number_pass += 1 
        else:
            number_no_pass += 1

    return number_pass,number_no_pass

# PROBLEMA 3
def get_final_prom(students:list) -> float:
    """[get prom of all students]

    Args:
        students (list): [students list]

    Returns:
        float: [final prom]
    """
    grade_final_course = [student.get_prom() for student in students]
    return sum(grade_final_course) / len(grade_final_course)  

# PROBLEMA 4
def get_compare_prom(students: list) -> tuple:
    """[get student with higher prom and lowe prom]

    Args:
        students ([list]): [students list]

    Returns:
        [tuple]: [0 -> student with prom high, 1 -> student with prom low]
    """
    grade_final_course = [student.get_prom() for student in students]
    prom_high = max(grade_final_course)
    prom_low = min(grade_final_course)

    student_high = students[grade_final_course.index(prom_high)]
    studen_low = students[grade_final_course.index(prom_low)]
    return student_high, studen_low

# PROBLEMA 5
def find_student(students:list, search_name:str) -> list:
    """[get names that have search_name in self]

    Args:
        students ([list]): [students list]
        search_name ([str]): [name to search]

    Returns:
        [list]: [list students match]
    """
    return [student for student in students if search_name in student.name]


students = enter_students(3)

print(students)
print(get_number_pass_no(students))
print("Final prom:",get_final_prom(students))

students_prom = get_compare_prom(students)
print("PROM HIGH:",students_prom[0].name)
print("PROM LOW:",students_prom[1].name)

final_students = find_student(students,"ricardo")

for student in final_students:
    print("NAME:",student.name)
    print("GRADES:",student.grades)