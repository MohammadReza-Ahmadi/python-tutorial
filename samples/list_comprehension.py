a = [1, 3, 5, 7, 9, 11]
print("a=", a)
c = []
for x in a:
    c.append(x * 2)

print(c)

# now do up increase using list comprehension:
d = [x * 2 for x in a]
print(d)

d = [x * 3 for x in a]
print(d)

d = [x ** 2 for x in a]
print(d)

d = [x ** 2 for x in range(2, 5)]
print(d)

print("---- create a descending range:")
for x in range(6, 0, -1):
    print(x)

print("------ create squared list:")
f1 = []
for x in range(6, 0, -1):
    f1.append(x ** 2)
print(f1)

print("------ create squared list by list comprehensive:")
f2 = [x ** 2 for x in range(6, 0, -1)]
print(f2)
