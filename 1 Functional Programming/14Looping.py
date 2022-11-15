# Loops allows us to execute a statement multiple times. there are total two types of loops in python : for loop and while loop...

# 1. FOR LOOP ---> 
for num in range(0,100):
    print(num)

start = int(input())
end = int(input())
for num in range(start, end):
    print(num)

for num in range(0,1000,3):
    print(num)

# 2. WHILE LOOP --->
var = int(input("ENTER TABLE CALCULATION VALUE"))
i = 1
while(i <= 10):
    print(var * i)
    i = i + 1
