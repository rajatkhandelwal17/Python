print("ENTER FIRST NUMBER")
a = int(input())
print("ENTER SECOND NUMBER")
b = int(input())
a = a ^ b
b = a ^ b
a = a ^ b
print("VALUE OF A IS = ", a)
print("VALUE OF B IS = ", b)