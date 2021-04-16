class File:
    def __init__(self, name):
        self.name = name

    def read_files(self):
        file = open("w")
        file.write(str(dict))
        file.close()
        print(dict)

f = File(10_03_2020)
print(f)
print(dict)


# def generator_a(second, first = 0, step = 1):
#     if first > second:
#         second, first = first, second
#     while second > first:
#         res = first
#         first += step
#         yield res
# gen_iter = generator_a(5, 10, 2)
# for i in gen_iter:
#     print(i)