class Employee:
    def __init__(self, name, surname, salary, department):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.department = department
    def show_info(self):
        print(f"name: {self.name}")
        print(f"Surname: {self.surname}")
        print(f"salary: {self.salary}")
        print(f"Department: {self.department}")
        print(f"*" * 15)
Employee1 = Employee("Rejep", "Orazow", 6000, "Gurtly")
Employee2 = Employee("Meret", "Ashyrow", 1000, "gazocak")
Employee3 = Employee("Daemon", "targaryen", 30000, "Westeros")
Employee4 = Employee("Baky", "Hojayyow", 900000, "Ashgabat")
Employee5 = Employee("Aegon", "targaryen", 30000, "Westeros")

Employee1.show_info()
Employee2.show_info()
Employee3.show_info()
Employee4.show_info()
Employee5.show_info()