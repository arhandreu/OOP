def average_grade(grad, course="all"):
    all_grades = []
    if course == "all":
        for grade in grad.values():
            all_grades += grade
        return sum(all_grades) / len(all_grades)
    else:
        return sum(grad[course]) / len(grad[course])


def average_grad_all(course, *units):
    sum_aver_grades = 0
    count_unit = 0
    for unit in units:
        sum_aver_grades += average_grade(unit.grades, course)
        count_unit += 1
    return sum_aver_grades / count_unit


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.courses_in_progress.append(course_name)

    def rate_lector(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {average_grade(self.grades)} \n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)} \n'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Это не студент!")
            return
        return average_grade(self.grades) > average_grade(other.grades)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def add_courses(self, course_name):
        self.courses_attached.append(course_name)


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {average_grade(self.grades)}\n'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Это не лектор!")
            return
        return average_grade(self.grades) < average_grade(other.grades)


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}\n'


student_1 = Student('Andrey', 'Bardukov', 'Men')
student_1.courses_in_progress += ['Biology', 'History', 'Physics']
student_1.add_courses('Music')

student_2 = Student('Sergei', 'Morozov', 'Men')
student_2.courses_in_progress += ['History', 'Physics', 'Biology', 'Music']

review_1 = Reviewer('Review', '_1')
review_1.add_courses('History')
review_1.add_courses('Physics')
review_2 = Reviewer('Review', '_2')
review_2.add_courses('Music')
review_2.add_courses('Biology')

lector_1 = Lecturer('Lector', '_1')
lector_1.add_courses('Music')
lector_1.add_courses('Biology')
lector_1.add_courses('History')
lector_1.add_courses('Physics')
lector_2 = Lecturer('Lector', '_2')
lector_2.add_courses('History')
lector_2.add_courses('Physics')
lector_2.add_courses('Music')
lector_2.add_courses('Biology')

student_1.rate_lector(lector_1, 'Music', 8)
student_1.rate_lector(lector_2, 'History', 5)
student_2.rate_lector(lector_2, 'Physics', 4)
student_2.rate_lector(lector_1, 'Biology', 2)
student_1.rate_lector(lector_1, 'Music', 2)
student_1.rate_lector(lector_2, 'History', 3)
student_2.rate_lector(lector_2, 'Physics', 5)
student_2.rate_lector(lector_1, 'Biology', 7)
student_1.rate_lector(lector_2, 'Music', 4)
student_1.rate_lector(lector_1, 'History', 5)
student_2.rate_lector(lector_1, 'Physics', 4)
student_2.rate_lector(lector_2, 'Biology', 2)
student_1.rate_lector(lector_2, 'Music', 2)
student_1.rate_lector(lector_1, 'History', 3)
student_2.rate_lector(lector_1, 'Physics', 5)
student_2.rate_lector(lector_2, 'Biology', 7)

review_2.rate_hw(student_1, 'Music', 5)
review_1.rate_hw(student_1, 'History', 4)
review_1.rate_hw(student_1, 'Physics', 7)
review_2.rate_hw(student_1, 'Biology', 9)

review_2.rate_hw(student_2, 'Music', 8)
review_1.rate_hw(student_2, 'History', 7)
review_1.rate_hw(student_2, 'Physics', 6)
review_2.rate_hw(student_2, 'Biology', 10)


print(review_2)
print(student_2)
print(lector_1)
print(lector_2)
print(lector_1 > lector_2)
print(average_grad_all('History', student_2, student_1))
print(average_grad_all('Biology', lector_1, lector_2))
