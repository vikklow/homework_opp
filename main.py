class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_grade = 0

    def __str__(self):
        base_info = super().__str__()
        return (f"{base_info}\nСредняя оценка за лекции: "
                f"{self.average_grade:.1f}")

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade < other.average_grade
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade <= other.average_grade
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade == other.average_grade
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade > other.average_grade
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade >= other.average_grade
        return NotImplemented

    def calculate_average_grade(self):
        if not self.grades:
            self.average_grade = 0
            return
        total_sum = 0
        total_count = 0
        for course_grades in self.grades.values():
            total_sum += sum(course_grades)
            total_count += len(course_grades)
        self.average_grade = (
            total_sum / total_count if total_count > 0 else 0
        )


class Reviewer(Mentor):

    def rate_hw(self, student_obj, course, grade):
        if (isinstance(student_obj, Student) and
                course in self.courses_attached and
                course in student_obj.courses_in_progress):
            if course not in student_obj.grades:
                student_obj.grades[course] = []
            student_obj.grades[course].append(grade)
            student_obj.calculate_average_grade()
            return True
        else:
            print("Ошибка: невозможно поставить оценку")
            return False


class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade = 0

    def __str__(self):
        courses_in_progress_str = (
            ', '.join(self.courses_in_progress)
            if self.courses_in_progress else "Нет"
        )
        finished_courses_str = (
            ', '.join(self.finished_courses)
            if self.finished_courses else "Нет"
        )
        return (
            f"Имя: {self.name}\nФамилия: {self.surname}\n"
            f"Средняя оценка за домашние задания: "
            f"{self.average_grade:.1f}\nКурсы в процессе изучения: "
            f"{courses_in_progress_str}\nЗавершенные курсы: "
            f"{finished_courses_str}"
        )

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade < other.average_grade
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Student):
            return self.average_grade <= other.average_grade
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_grade == other.average_grade
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.average_grade > other.average_grade
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Student):
            return self.average_grade >= other.average_grade
        return NotImplemented

    def rate_lecture(self, lecturer_obj, course, grade):
        if not isinstance(lecturer_obj, Lecturer):
            print("Ошибка: можно оценивать только лекторов")
            return False
        if course not in self.courses_in_progress:
            print(f"Ошибка: студент не изучает курс '{course}'")
            return False
        if course not in lecturer_obj.courses_attached:
            print(f"Ошибка: лектор не прикреплен к курсу '{course}'")
            return False
        if grade < 0 or grade > 10:
            print("Ошибка: оценка должна быть от 0 до 10")
            return False

        if course not in lecturer_obj.grades:
            lecturer_obj.grades[course] = []
        lecturer_obj.grades[course].append(grade)
        lecturer_obj.calculate_average_grade()
        return True

    def calculate_average_grade(self):
        if not self.grades:
            self.average_grade = 0
            return
        total_sum = 0
        total_count = 0
        for course_grades in self.grades.values():
            total_sum += sum(course_grades)
            total_count += len(course_grades)
        self.average_grade = (
            total_sum / total_count if total_count > 0 else 0
        )


def average_hw_grade(students, course):
    total_sum = 0
    total_count = 0
    for student in students:
        if course in student.grades:
            total_sum += sum(student.grades[course])
            total_count += len(student.grades[course])
    return total_sum / total_count if total_count > 0 else 0


def average_lecture_grade(lecturers, course):
    total_sum = 0
    total_count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_sum += sum(lecturer.grades[course])
            total_count += len(lecturer.grades[course])
    return total_sum / total_count if total_count > 0 else 0


if __name__ == "__main__":

    lecturer1 = Lecturer('Иван', 'Иванов')
    lecturer2 = Lecturer('Петр', 'Петров')

    reviewer1 = Reviewer('Анна', 'Смирнова')
    reviewer2 = Reviewer('Сергей', 'Кузнецов')

    student1 = Student('Мария', 'Сидорова', 'Ж')
    student2 = Student('Алексей', 'Попов', 'М')

    lecturer1.courses_attached += ['Python', 'Git']
    lecturer2.courses_attached += ['Python', 'Java']

    reviewer1.courses_attached += ['Python', 'Git']
    reviewer2.courses_attached += ['Java', 'C++']

    student1.courses_in_progress += ['Python', 'Git']
    student1.finished_courses += ['Введение в программирование']

    student2.courses_in_progress += ['Python', 'Java']
    student2.finished_courses += ['Алгоритмы']

print("\nЗадание №1:")
print(f"\nlecturer1 - экземпляр Mentor: {isinstance(lecturer1, Mentor)}")
print(f"reviewer1 - экземпляр Mentor: {isinstance(reviewer1, Mentor)}")
print(f"lecturer1.courses_attached: {lecturer1.courses_attached}")
print(f"reviewer1.courses_attached: {reviewer1.courses_attached}")

print("\nЗадание №2:")
print("\nПроверяющий выставляет оценки студентам:")
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student1, 'Git', 10)
reviewer1.rate_hw(student2, 'Python', 7)

print("\nСтуденты оценивают лекции:")
student1.rate_lecture(lecturer1, 'Python', 9)
student1.rate_lecture(lecturer1, 'Python', 8)
student2.rate_lecture(lecturer1, 'Python', 10)
student2.rate_lecture(lecturer2, 'Python', 8)

print("\nПроверка обработки ошибок:")
student1.rate_lecture(lecturer1, 'Java', 8)
student1.rate_lecture(lecturer1, 'C++', 8)
student1.rate_lecture(reviewer1, 'Python', 6)

print("\nЗадание №3:")
print("\nИнформация о проверяющем:")
print(reviewer1)

print("\nИнформация о лекторе:")
print(lecturer1)

print("\nИнформация о студенте:")
print(student1)

print("\nСравнение студентов по средней оценке:")
student1.calculate_average_grade()
student2.calculate_average_grade()
print(f"student1 > student2: {student1 > student2}")
print(f"student1 < student2: {student1 < student2}")
print(f"student1 == student2: {student1 == student2}")

print("\nСравнение лекторов по средней оценке:")
lecturer1.calculate_average_grade()
lecturer2.calculate_average_grade()
print(f"lecturer1 > lecturer2: {lecturer1 > lecturer2}")
print(f"lecturer1 < lecturer2: {lecturer1 < lecturer2}")
print(f"lecturer1 == lecturer2: {lecturer1 == lecturer2}")

print("\nЗадание №4:")
students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]

avg_hw_python = average_hw_grade(students_list, 'Python')
avg_lecture_python = average_lecture_grade(lecturers_list, 'Python')

print(f"\nСредняя оценка за ДЗ по курсу 'Python': {avg_hw_python:.1f}")
print(f"Средняя оценка за лекции по курсу 'Python': {avg_lecture_python:.1f}")

print("\nПроверка всех созданных объектов:")
print("\nВсе лекторы:")
for idx, lect in enumerate([lecturer1, lecturer2], 1):
    print(f"\nЛектор {idx}:")
    print(lect)

print("\nВсе проверяющие:")
for idx, rev in enumerate([reviewer1, reviewer2], 1):
    print(f"\nПроверяющий {idx}:")
    print(rev)

print("\nВсе студенты:")
for idx, stud in enumerate([student1, student2], 1):
    print(f"\nСтудент {idx}:")
    print(stud)