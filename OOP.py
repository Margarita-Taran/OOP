class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lect(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in
                lecturer.courses_attached and 0 <= grade <= 10):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rating(self):
        result = 0
        if self.grades:
            for grade in self.grades.values():
                result += sum(grade) / len(grade)
            return round(result / len(self.grades), 1)
        else:
            return 0

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.average_rating()}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.average_rating() > other.average_rating()
        print('Ошибка')
        return

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_rating() < other.average_rating()
        print('Ошибка')
        return


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_rating(self):
        result = 0
        if self.grades:
            for grade in self.grades.values():
                result += sum(grade) / len(grade)
            return round(result / len(self.grades), 1)
        else:
            return 0

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating()}'

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_rating() > other.average_rating()
        print('Ошибка')
        return

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_rating() < other.average_rating()
        print('Ошибка')
        return


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached and course in
                student.courses_in_progress and 0 <= grade <= 10):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение в программирование']
student_2 = Student('Ivan', 'Ivanov', 'your_gender')
student_2.courses_in_progress += ['Python', 'Git']
student_2.finished_courses += ['Введение в программирование']

mentor_1 = Lecturer('Some', 'Buddy')
mentor_1.courses_attached += ['Python', 'Git']
mentor_2 = Lecturer('Gleb', 'Smirnov')
mentor_2.courses_attached += ['Python', 'Git']

mentor_3 = Reviewer('Agata', 'Li')
mentor_3.courses_attached += ['Python', 'Git']
mentor_4 = Reviewer('Roman', 'Markov')
mentor_4.courses_attached += ['Python', 'Git']

student_1.rate_lect(mentor_1, 'Python', 6)
student_1.rate_lect(mentor_1, 'Python', 10)
student_1.rate_lect(mentor_1, 'Python', 7)

student_1.rate_lect(mentor_1, 'Git', 7)
student_1.rate_lect(mentor_1, 'Git', 5)
student_1.rate_lect(mentor_1, 'Git', 9)

student_1.rate_lect(mentor_2, 'Python', 7)
student_1.rate_lect(mentor_2, 'Python', 8)
student_1.rate_lect(mentor_2, 'Python', 10)

student_1.rate_lect(mentor_2, 'Git', 6)
student_1.rate_lect(mentor_2, 'Git', 5)
student_1.rate_lect(mentor_2, 'Git', 4)

student_2.rate_lect(mentor_1, 'Python', 6)
student_2.rate_lect(mentor_1, 'Python', 8)
student_2.rate_lect(mentor_1, 'Python', 8)

student_2.rate_lect(mentor_1, 'Git', 7)
student_2.rate_lect(mentor_1, 'Git', 9)
student_2.rate_lect(mentor_1, 'Git', 10)

student_2.rate_lect(mentor_2, 'Python', 7)
student_2.rate_lect(mentor_2, 'Python', 9)
student_2.rate_lect(mentor_2, 'Python', 7)

student_2.rate_lect(mentor_2, 'Git', 8)
student_2.rate_lect(mentor_2, 'Git', 8)
student_2.rate_lect(mentor_2, 'Git', 5)

mentor_3.rate_hw(student_1, 'Python', 10)
mentor_3.rate_hw(student_1, 'Python', 10)
mentor_3.rate_hw(student_1, 'Python', 10)

mentor_3.rate_hw(student_1, 'Git', 8)
mentor_3.rate_hw(student_1, 'Git', 5)
mentor_3.rate_hw(student_1, 'Git', 6)

mentor_3.rate_hw(student_2, 'Python', 8)
mentor_3.rate_hw(student_2, 'Python', 10)
mentor_3.rate_hw(student_2, 'Python', 7)

mentor_4.rate_hw(student_2, 'Git', 9)
mentor_4.rate_hw(student_2, 'Git', 7)
mentor_4.rate_hw(student_2, 'Git', 10)

mentor_4.rate_hw(student_1, 'Python', 6)
mentor_4.rate_hw(student_1, 'Python', 5)
mentor_4.rate_hw(student_1, 'Python', 8)

mentor_4.rate_hw(student_1, 'Git', 6)
mentor_4.rate_hw(student_1, 'Git', 5)
mentor_4.rate_hw(student_1, 'Git', 4)

mentor_4.rate_hw(student_2, 'Python', 10)
mentor_4.rate_hw(student_2, 'Python', 10)
mentor_4.rate_hw(student_2, 'Python', 8)

mentor_4.rate_hw(student_2, 'Git', 8)
mentor_4.rate_hw(student_2, 'Git', 4)
mentor_4.rate_hw(student_2, 'Git', 7)


print(f'Список студентов:\n{student_1}\n\n{student_2}')
print()
print(student_1.__gt__(student_2))
print(student_1.__lt__(student_2))
print()
print(f'Список лекторов:\n{mentor_1}\n\n{mentor_2}')
print()
print(mentor_1.__gt__(mentor_2))
print(mentor_1.__lt__(mentor_2))
print()
print(f'Список проверяющих:\n{mentor_3}\n\n{mentor_4}')

students = [student_1, student_2]
lecturers = [mentor_1, mentor_2]


def average_student_grade(students, course):
    total_grade = 0
    count_students = 0
    for student in students:
        if course in student.courses_in_progress and course in student.grades:
            total_grade += sum(student.grades[course])
            count_students += len(student.grades[course])
    if count_students > 0:
        average_grade = total_grade / count_students
        return round(average_grade, 1)
    else:
        return 0


def average_lecturer_grade(lecturers, course):
    total_grade = 0
    count_lecturers = 0
    for lecturer in lecturers:
        if course in lecturer.courses_attached and course in lecturer.grades:
            total_grade += sum(lecturer.grades[course])
            count_lecturers += len(lecturer.grades[course])
    if count_lecturers > 0:
        average_grade = total_grade / count_lecturers
        return round(average_grade, 1)
    else:
        return 0


print()
print(f'Средняя оценка по всем студентам за домашние задания по курсу {"Python"}: '
      f'{average_student_grade(students,"Python")}')
print(f'Средняя оценка за лекции всех лекторов по курсу {"Python"}: '
      f'{average_lecturer_grade(lecturers,"Python")}')
