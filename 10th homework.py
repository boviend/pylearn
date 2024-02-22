# клас для опису товару (значення ціни, опис, габарити товару)

class Item:
    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        return f"{self.name}, price: {self.price}$"


# декілька екземплярів класу + tests

product1 = Item(price=100, description="Smartphone", dimensions="15x7x1 cm", name="iphone 15")
product2 = Item(price=50, description="Headphones", dimensions="20x15x8 cm", name="beats")
product3 = Item(price=30, description="Notebook", dimensions="30x22x2 cm", name="air")

print(f"Random params: {product1.price} {product2.description} {product3.name}")
print(product1)


# клас "Покупець" ( прізвище, ім'я, по батькові, мобільний телефон і т.д.)

class User:

    def __init__(self, name, surname, number, *args):
        self.name = name
        self.surname = surname
        self.number = number

    def __str__(self):
        return f"{self.name}, na prizvisko: {self.surname}"


User1 = User("Mykola", "Shtanko", 99)
print(User1)  # user1


# клас "Замовлення"(кілька товарів, "підв'язане" до користувача, метод обчислення сумарної вартості замовлення)

class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def __str__(self):
        items_str = "\n".join([f"{item.name}: {cnt}pcs." for item, cnt in self.products.items()])
        return f'"""\nUser: {self.user.name} {self.user.surname}\nItems:\n{items_str}\nTotal cost: {self.get_total()}$\n"""'

    def get_total(self):
        for item, cnt in self.products.items():
            self.total += item.price * cnt
        return self.total


cart = Purchase(User1)
cart.add_item(product1, 4)
cart.add_item(product2, 20)
print(cart)


class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, Record Book: {self.record_book}"


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
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
        all_students = "\n".join(str(student) for student in self.group)
        return f"Number: {self.number}\n{all_students}"


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
print(gr.find_student('Jobs'))  # 'Steve Jobs'
print(gr.find_student('Jobs2'))  # None

gr.delete_student('Taylor')
print(gr)  # Only one student
