class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"gender = {self.gender}, age = {self.age}, first_name = {self.first_name}, last_name = {self.last_name}"

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"Students: {super().__str__()}, record_book = {self.record_book}"
class BigGroupError(Exception):
    pass

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)

    def __str__(self):
        all_students = ''
        n = 1
        for student in self.group:
            if n>10:
                raise BigGroupError(' <<  This group is full  >>')
            all_students += f"{n}){str(student.last_name)}.\n"
            n += 1
        return f'Number:{self.number}\n{all_students} '


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 32, 'Stee', 'Joli', 'AN143')
st4 = Student('Female', 24, 'Li', 'Tay', 'AN146')
st5 = Student('Male', 31, 'Bobe', 'Djager', 'AN141')
st6 = Student('Female', 23, 'Sam', 'Dogger', 'AN150')
st7 = Student('Male', 30, 'Joe', 'Tribiani', 'AN144')
st8 = Student('Female', 26, 'Sisilia', 'Kudrou', 'AN147')
st9 = Student('Male', 33, 'Franck', 'Big', 'AN148')
st10 = Student('Female', 28, 'Nenci', 'Cuper', 'AN149')
st11 = Student('Female', 31, 'Kait', 'Zizibaba', 'AN151')
st12 = Student('Male', 35, 'Tim', 'Getsbi', 'AN154')
gr = Group('PD1')
gr.add_student(st1), gr.add_student(st2), gr.add_student(st3), gr.add_student(st4), gr.add_student(st5)
gr.add_student(st6), gr.add_student(st7), gr.add_student(st8), gr.add_student(st9), gr.add_student(st10)
#gr.add_student(st11), gr.add_student(st12)
print(gr)