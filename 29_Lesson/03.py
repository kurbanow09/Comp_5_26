class car:
    def __init__(self, model, color, year, speed):
        self.model = model
        self.color = color
        self.year = year
        self.speed = speed
    def show_info(self):
        print(f"model: {self.model}")
        print(f"color: {self.color}")
        print(f"year: {self.year}")
        print(f"speed: {self.speed}")
        print(f"*" * 15)
    def speed_up(self):
        self.speed += 10
        print(f"Speed_up: method: {self.speed}")
car = car("Toyota", "White", 2014, 70,)

car.show_info()
car.speed_up()
car.speed_up()
car.speed_up()