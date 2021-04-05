class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def update(self, **kwargs):
        if kwargs.get('name'):
            self.__name = kwargs['name']
        if kwargs.get('age'):
            self.__age = kwargs['age']

    def get_info(self):
        return "{}, age: {}".format(self.__name, self.__age)


class Note:

    def __init__(self):
        self.__note_list = list()

    def add_person(self, person):
        self.__note_list.append(person)

    def remove_person(self, index):
        if 0 <= index <= len(self.__note_list)-1:
            self.__note_list.remove(self.__note_list[index])

    def update_person(self, index, **kwargs):
        if 0 <= index <= len(self.__note_list)-1:
            person = self.__note_list[index]
            person.update(**kwargs)

    def get_info_note(self):
        result = list()
        for i in self.__note_list:
            result.append(i.get_info())
        return result

class Index(Person):
    def result(self, index):
        print(self.name, "Index :", index)

note = Note()

index1 = Index('Ivan', 24)
index2 = Index('Ivan1', 23)
index3 = Index('Ivan2', 25)
index4 = Index('Ivan3', 26)

note.add_person(index1)
note.add_person(index2)
note.add_person(index3)
note.add_person(index4)

print(note.get_info_note())

index1.result("a")
index2.result("b")
index3.result("c")
index4.result("d")

note.remove_person(2)
print(note.get_info_note())

note.update_person(1, name='Jon', age=15)

index1.result("z")
index2.result("d")
index3.result("e")
index4.result("f")

print(note.get_info_note())