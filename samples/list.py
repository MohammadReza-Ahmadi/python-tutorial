


a=[1,-4,0,-12,5,17]

print(a)

a.append(23)
print(a)

a.append("hello")
print(a)

a.append(["second-list",28,'a'])
print(a)

a.pop()
print(a)
a.pop()
print(a)

print(a[0])
print(a[3])
print(a[5])

a[5] = 100
print(a[5])

b = ["one","two","tree"]
print(b)
b[0],b[2]=b[2],b[0]
print(b)
