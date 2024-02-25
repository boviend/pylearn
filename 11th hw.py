class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.record_book}'


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise Exception("The group is full. Cannot add more than 10 students.")
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = ', '.join([str(student) for student in self.group])
        return f'Number: {self.number}\nStudents: {all_students}'


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st4 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st5 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
sth6 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st7 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st8 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st9 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st10 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st11 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(sth6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)
# gr.add_student(st11)
print(gr)
print(gr.find_student('Jobs'))  # 'Steve Jobs'
print(gr.find_student('Jobs2'))  # None
gr.delete_student('Taylor')
print(gr)  # Only one student
print(id(st10))


#   test 2

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.get_square() == other.get_square()

    def __add__(self, other):
        new_width = self.width + other.width
        new_height = self.height + other.height
        return Rectangle(new_width, new_height)

    def __mul__(self, n):
        new_width = self.width * n
        new_height = self.height * n
        return Rectangle(new_width, new_height)

    def __str__(self):
        return f"Rectangle (width={self.width}, height={self.height})"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8
assert r2.get_square() == 18

r3 = r1 + r2
assert r3.get_square() == 26

r4 = r1 * 4
assert r4.get_square() == 32
