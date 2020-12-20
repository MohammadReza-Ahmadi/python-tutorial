

d = {}
d["one"]=100
d["two"]=200
print(d["one"])
print(d["two"])

a = dict()
a["first"]=500
a["second"]=700
print(a["first"])
print(a["second"])

b = {"name":"ali","age":32}
print(b["name"])
print(b["age"])

print("---- for by key and values print: -------")
b = {"name":"ali","age":32,"key1":1, "key2":"val2","key3":24.56}
for key, value in b.items():
    print("key=",key)
    print("val=",value)
