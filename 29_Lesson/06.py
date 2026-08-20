class Student:

  def __init__(self, name, surname, age):
    self.name = name
    self.surname = surname
    self.age = age

  def show_info(self):
    print(f"Name: {self.name}")
    print(f"Surname: {self.surname}")
    print(f"Age: {self.age}")
    print("*" * 25)


students_list = []

while True:
  user_input = input("Adynyzy giriz (stop): ").strip()

  if user_input.lower() == "stop":
    break

  name = user_input.capitalize()
  surname = input("Familiyanyz: ").capitalize()
  age = input("yasynyz: ")

  stu = Student(name, surname, age)
  students_list.append(stu)

print("\nOkuwcylaryn sanawy")
for student in students_list:
  student.show_info()