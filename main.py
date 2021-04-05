# 1
class Human:
    def __init__(self, name, phone, age, city, birthday):
        self.name = name
        self.phone = phone
        self.age = age
        self.city = city
        self.birthday = birthday
    def walk(self):
        print("I can walk! ")
    def watch(self):
        print("I can see")
    def jump(self):
        print("I can jump")
    def getinfo(self):
        print(self.name)
        print(self.age)
        print(self.city)
        print(self.phone)
        print(self.birthday)
human1 = Human("Alex", "2938374823", "33", "London", "19.07.1988")
human2 = Human("Lena", "1293712983", "20", "Kiev", "27.02.2001")
human3 = Human("Dima", "7412982443", "31", "Rio-De-Janeiro", "10.01.1990")
print(human1)
human1.getinfo()
human1.walk()
human1.jump()
print("__________")
print(human2)
human2.getinfo()
human2.watch()
human2.jump()
print("----------")
human3.getinfo()
human3.walk()
human3.watch()
#
# # 2
# number11 = float(input("Введите первое значение: "))
# number22 = float(input("Введите второе значение: "))
# operation1 = str(input("Введите операцию: "))
# class Calculator:
#     def __init__(self, number1, number2, operation):
#         self.number1 = number1
#         self.number2 = number2
#         self.operation = operation
#     def plus(self):
#         res1 = self.number1 + self.number2
#         return res1
#     def minus(self):
#         res2 = self.number1 - self.number2
#         return res2
#     def multipl(self):
#         res3 = self.number1 * self.number2
#         return res3
#     def division(self):
#         res4 = self.number1 / self.number2
#         return res4
#     def result(self):
#         if self.operation == "+":
#             res = self.plus()
#             return res
#         elif self.operation == "-":
#             res = self.minus()
#             return res
#         elif self.operation == "*":
#             res = self.multipl()
#             return res
#         else:
#             res = self.division()
#             return res
# calc = Calculator(number11, number22, operation1)
# print(calc.result())

# # 3
# class Human:
#     list_person = []
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
#
#
#     def convert_to_dict(self):
#         return {"name": self.name, "surname": self.surname, "age": self.age}
#
#
#     def check_in_list(self):
#         for i in self.list_person:
#             if self.name and self.surname and self.age in self.list_person:
#                 self.list_person.append(self, i)
#             else:
#                 self.list_person.append(self, i)
#                 return self.list_person
#     # def add_to_list(self):
#     #     Human.list_person.append(human1.convert_to_dict())
#
#
# human1 = Human("Ivan", "Ivanov", 32)
# human2 = Human("Ivan", "Ivanov", 32)
# human3 = Human("Petr", "Antonov", 24)
# human4 = Human("Petr", "Antonov", 24)
#
#
# Human.list_person.append(human1.convert_to_dict())
# Human.list_person.append(human2.convert_to_dict())
# Human.list_person.append(human3.convert_to_dict())
# Human.list_person.append(human4.convert_to_dict())
# print(Human.list_person)