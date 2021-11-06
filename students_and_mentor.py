class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def lecturer_rate(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress \
                and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def middle_grade(self):
        rate = 0
        count = 0
        for value in self.grades.values():
            for i in value:
                rate = rate + int(i)
                count += 1
            result = round((rate / count), 2)
        return result

    def __lt__(self, student):
        if not isinstance(student, Student):
            return
        return self.middle_grade() < student.middle_grade()

    def __str__(self):
        progress = ', '.join(self.courses_in_progress)
        finished = ', '.join(self.finished_courses)
        middle = self.middle_grade()
        result = f'Имя: {self.name}\n' \
                 f'Фамилия: {self.surname}\n' \
                 f'Средняя оценка: {middle}\n' \
                 f'Курсы в процессе изучения: {progress}\n' \
                 f'Завершенные курсы: {finished}'
        return result


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_attached = []

    def __lt__(self, lecturer):
        if not isinstance(lecturer, Lecturer):
            return
        return Student.middle_grade(self) < Student.middle_grade(lecturer)

    def __str__(self):
        middle = Student.middle_grade(self)
        result = f'Имя: {self.name}\n' \
                 f'Фамилия: {self.surname}\n' \
                 f'Средняя оценка: {middle}'
        return result


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached \
                and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        result = f'Имя: {self.name}\n' \
                 f'Фамилия: {self.surname}'
        return result


def student_middle_rate(students_list, course):
    count = 0
    rate = 0
    for student in students_list:
        if course in student.grades:
            for i in student.grades[course]:
                rate = rate + int(i)
                count += 1
    rate = round((rate / count), 2)
    return rate


def lecturer_middle_rate(lecturers_list, course):
    count = 0
    rate = 0
    for lecturer in lecturers_list:
        if course in lecturer.grades:
            for i in lecturer.grades[course]:
                rate = rate + int(i)
                count += 1
    rate = round((rate / count), 2)
    return rate


first_student = Student('Ruoy', 'Eman', 'your_gender')
first_student.courses_in_progress += ['Java']
first_student.courses_in_progress += ['Python']
first_student.courses_in_progress += ['JS']
first_student.finished_courses += ['Basic']

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Java']
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Kotlin']

some_reviewer.rate_hw(first_student, 'Python', 8)
some_reviewer.rate_hw(first_student, 'Python', 10)
some_reviewer.rate_hw(first_student, 'Python', 7)
some_reviewer.rate_hw(first_student, 'Java', 9)
some_reviewer.rate_hw(first_student, 'Java', 8)
some_reviewer.rate_hw(first_student, 'Kotlin', 7)

first_lecturer = Lecturer('Tom', 'Rodgers')
first_lecturer.courses_attached += ['Python']
first_lecturer.courses_attached += ['JS']

first_student.lecturer_rate(first_lecturer, 'Python', 10)
first_student.lecturer_rate(first_lecturer, 'JS', 9)
first_student.lecturer_rate(first_lecturer, 'Python', 8)
first_student.lecturer_rate(first_lecturer, 'JS', 7)

second_student = Student('Bill', 'Wild', 'men')
second_student.courses_in_progress += ['Java']
some_reviewer.rate_hw(second_student, 'Java', 7)

second_lecturer = Lecturer('John', 'Stone')
second_lecturer.courses_attached += ['Java']
second_lecturer.courses_attached += ['Python']

second_student.lecturer_rate(second_lecturer, 'Python', 9)
second_student.lecturer_rate(second_lecturer, 'Java', 8)

students_list = [first_student, second_student]
lecturers_list = [first_lecturer, second_lecturer]

student_mid_rate = student_middle_rate(students_list, 'Java')
lecturer_mid_rate = lecturer_middle_rate(lecturers_list, 'Python')

print(some_reviewer)
print('---')
print(second_lecturer)
print('---')
print(first_student)
print('---')
print(f'Средняя оценка за домашние задания по всем студентам: {student_mid_rate}')
print(f'Средняя оценка за лекции всех лекторов: {lecturer_mid_rate}')
print(f'Сравнение двух лекторов: '
      f'{Student.middle_grade(second_lecturer)} < '
      f'{Student.middle_grade(first_lecturer)} = '
      f'{second_lecturer < first_lecturer}')
print(f'Сравнение двух студентов: '
      f'{Student.middle_grade(first_student)} < '
      f'{Student.middle_grade(second_student)} = '
      f'{first_student < second_student}')
