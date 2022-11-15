a = 5
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))

a = 1+2j
print(a, "is complex number?", isinstance(1+2j,complex))

a = [1, 2.2, 'python']
print(a, "is of type", type(a))

t = (5,'program', 1+3j)
print(t, "is of type", type(t))

s = "This is a string"
print(s, "is of type", type(s))

a = {5,2,3,1,4}
print(a, "is of type", type(a))

d = {1:'value','key':2}
print(d, "is of type", type(d))
