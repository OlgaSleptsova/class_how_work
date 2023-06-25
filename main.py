


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)


    def rate_lc(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average(self):
       f = self.grades.values()
       g = list(f)
       m=[]
       for x in g:
           for f in x:
               m.append(f)
       average = sum(m)//len(m)
       return average

    def __str__(self):
        text = f"Имя:{self.name}\nФамилия:{self.surname}\n Средняя оценка за домашние задания{self._average()}\n Курсы в процессе изучения:{','.join(self.courses_in_progress)}\n Завершенные курсы:{','.join(self.finished_courses)}"
        return text

    def __lt__(self, other):
        if not isinstance(other, Student):

            return "Not a Student"
        else:
            return self._average() < other._average()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
   grades = {}
   def _average(self):
       f = self.grades.values()
       g = list(f)
       m=[]
       for x in g:
           for f in x:
               m.append(f)
       average = sum(m)//len(m)
       return average



   def __str__(self):
       text =f"Имя:{self.name}\nФамилия:{self.surname}\nСредняя оценка за лекцию:{self._average()}"
       return text

   def __lt__(self, other):
       if not isinstance(other, Lecturer):

           return "Not a Lecture"
       return self._average() < other._average()
#
class Reviewe(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        res =f"Имя:{self.name}\nФамилия:{self.surname}"
        return res




best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Php']
best_student.courses_in_progress += ['CSS']
best_student.finished_courses +=['Введение в программирование']
best_student1 = Student('OLeg', 'Eman', 'your_gender')
best_student1.courses_in_progress += ['Php']
best_student1.courses_in_progress += ['Python']
best_student1.courses_in_progress += ['CSS']
best_student1.finished_courses +=['Введение в программирование']


olga = Reviewe('Some', 'Buddy')
olga.courses_attached += ['Python']
olga.courses_attached += ['Php']
olga.rate_hw(best_student, 'Python', 7)
olga.rate_hw(best_student, 'Php', 10)
olga.rate_hw(best_student1, 'Python', 10)

review=Reviewe('Димитрий','Корнеев')
review.courses_attached += ['Python']
review.courses_attached += ['Php']
review.rate_hw(best_student, 'Python', 10)
review.rate_hw(best_student, 'Php', 6)
review.rate_hw(best_student1, 'Python', 9)

# print(best_student.grades)
# print(best_student1.grades)

serg= Lecturer('Sergey', 'Tyrkov')
serg.courses_attached += ['Python']
serg.courses_attached += ['Php']
serg.courses_attached += ['CSS']
best_student.rate_lc(serg,'Python',7)
best_student.rate_lc(serg,'CSS',8)
best_student.rate_lc(serg,'Php',8)
best_student1.rate_lc(serg,'Python',10)
best_student1.rate_lc(serg,'CSS',10)
best_student1.rate_lc(serg,'Php',10)

lectur= Lecturer('Maxim', 'Belov')
lectur.courses_attached += ['Python']
lectur.courses_attached += ['Php']
lectur.courses_attached += ['CSS']
best_student.rate_lc(serg,'Python',9)
best_student.rate_lc(serg,'CSS',7)
best_student.rate_lc(serg,'Php',6)
best_student1.rate_lc(serg,'Python',8)
best_student1.rate_lc(serg,'CSS',7)
best_student1.rate_lc(serg,'Php',5)

# print(lectur)
#
# print(best_student<best_student1)
# print(serg<lectur)
students =[best_student,best_student1]

# cours = 'Python'
def average_GS(student,cours):
    list_grad =[]
    for student in students:
        if cours in student.grades.keys():
            for gr in  student.grades[cours]:
                list_grad.append(gr)

    aver_grad = sum(list_grad)//len(list_grad)
    return aver_grad

print(average_GS(students,'Python'))

lectures = [serg,lectur]
cours = 'Python'
def average_GL(lectures,cours):
    list_grad =[]
    for lect in lectures:
        if cours in lect.grades.keys():
            for gr in  lect.grades[cours]:
                list_grad.append(gr)

    aver_grad = sum(list_grad)//len(list_grad)
    return aver_grad
print(average_GL(lectures,'Python'))
