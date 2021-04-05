class Car:
    def __init__(self, driver, engine, mark_car):
        self.driver = driver
        self.engine = engine
        self.mark_car = mark_car

    def driver(self):
        print("My name: ")
    def engine(self):
        print("I have engine: ")
    def mark_car(self):
        print("Mark of car: ")
    def getinfo(self):
        print(self.driver)
        print(self.engine)
        print(self.mark_car)


class Driver(Car):
    def driver(self):
        


class Engine(Car):



car1 = Car("Alex", "v8", "BMW")
car2 = Car("Lena", "v6", "Audi")
car3 = Car("Dima", "v12", "Ford")
print(car1)
car1.getinfo()
car1.walk()
car1.jump()
print("__________")
print(car2)
car2.getinfo()
car2.watch()
car2.jump()
print("----------")
car3.getinfo()
car3.walk()
car3.watch()