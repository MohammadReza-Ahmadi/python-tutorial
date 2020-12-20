

a = set()
print(a)

a.add(1)
print(a)

a.add(2)
print(a)

a.add(2)
print(a)

for x in a:
    print(x)

print("--- define a mix value set:")
a = set()
a.add("one")
a.add(2)
a.add(True)
a.add("Four")
print(a)
a.add(2)
a.add("Four")
print(a)
a.add("One")
print(a)