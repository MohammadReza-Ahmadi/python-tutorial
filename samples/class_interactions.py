class Person:
    def __init__(self, n, p, i):
        self.name = n
        self.personality = p
        self.sitting = i

    def sit_down(self):
        self.sitting = True

    def stand_up(self):
        self.sitting = False


class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce(self):
        print("My name is: " + self.name)


r1 = Robot("Tom", "Red", 20)
p1 = Person("Alice", "aggressive", False)
p2 = Person("Becky", "talkative", True)
p2.robot_owned = r1

p2.robot_owned.introduce()