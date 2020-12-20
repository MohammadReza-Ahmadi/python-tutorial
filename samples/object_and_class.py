# print("define class without default constructor ..")
# class Robot:
#     def introduce(self):
#         print("My name is: "+self.name)
#
# r = Robot()
# r.name="Bobi"
# r.introduce()


print("Define class by constructor..")


class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce(self):
        print("My name is: "+self.name)


r1 = Robot("Tom", "Red", 20)
r2 = Robot("Gorges", "Green", 45)
print(r1)
print(r2)
print(r1.name)
print(r1.introduce())
print(r2.name)
print(r2.introduce())
