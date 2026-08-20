class Employee:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    def show_info(self):
        print(f"name: {self.name}")
        print(f"Surname: {self.surname}")
        print(f"Age: {self.age}")
        print(f"*" * 15)
Employee1 = Employee("Rejep", "Orazow", 33)
Employee2 = Employee("Meret", "Ashyrow", 25)
Employee3 = Employee("Daemon", "targaryen", 30)
Employee4 = Employee("Baky", "Hojayyow", 16)
Employee5 = Employee("Aegon", "targaryen", 31)

Employee1.show_info()
Employee2.show_info()
Employee3.show_info()
Employee4.show_info()
Employee5.show_info()