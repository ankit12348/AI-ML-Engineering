# name = "Ankit"
# message = f"Hello {name}"

# print(message)


# class User:
#     def __init__(self, name):
#         self.name = name


# user = User("Ankit")
# print(user.name)

# numbers = [1, 2, 3, 4, 5]
# result = [x * x for x in numbers]
# print(result)

# result = [x for x in numbers if x > 3]
# print(result)

# square = lambda x: x * x

# print(square(10))


class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def increment_salary(self, percent):
        self.salary += self.salary * percent / 100

    def display(self):
        print(self.id)
        print(self.name)
        print(self.salary)


# emp = Employee(101, "Ankit Giri", 100000)
# emp.increment_salary(10)
# emp.display()

employees = [
    Employee(100, "Ankit", 100000),
    Employee(101, "Mahima", 70000),
    Employee(102, "Asima", 25000),
    Employee(103, "Bandana", 80000),
    Employee(104, "Sujay", 100000),
]

employees.sort(key=lambda e: e.salary)
for e in employees:
    print(e.name)
