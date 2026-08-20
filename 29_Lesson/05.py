class people:
    def __init__(self, name, surname, age, phone):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone

    def show_info(self):
        print(f"name: {self.name}")
        print(f"Surname: {self.surname}")
        print(f"Age: {self.age}")
        print(f"Phone: {self.phone}")
        print(f"*" * 15)

    def new_age(self):
        self.age += 1
        print(f"Rejep New Age: {self.age}")

    def new_phone(self):
        self.phone += 100000
        print(f"Rejep New Age: {self.phone}")
people = people("Rejep", "Orazow", 18, 63625495)

people.show_info()
people.new_age()
people.new_phone()