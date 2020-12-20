

print(type("a text"))
print(type(123))
print(type(True))

if True:
    print("the True is true!!")

def are_you_sad(is_rainy,has_umbrella):
    return is_rainy and not has_umbrella

print(are_you_sad(True,False))
print(are_you_sad(True,True))