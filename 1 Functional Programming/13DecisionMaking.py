# Decision making is required when we want to execute a code only if a certain condition is satisfied. The if-elif-else statements is used in python for decision making like if , if-else, if-elif-else, nested if statements...

# 1. IF STATEMENT --->
num = int(input());
if num > 0: 
    print(f"{num} is a positive number")

# 2. IF - ELSE STATEMENT ---->
num1 = int(input())
if num > 0:
    print(f"{num1} is a positive number")
else:
    print(f"{num1} is negative number")

# 3. IF-ELIF-ELSE STATEMENT ---->
num2 = int(input())
if num2 > 0:
    print(f"{num2} is greater than zero")
elif num2 < 0:
    print(f"{num2} is less than zero")
else:
    print(f"{num2} num is equal to zero")

# 4. NESTED IF STATEMENTS ---->
num3 = int(input())
if num3 > 0:
    if num3 > 10:
        print(f"{num3} is greater than zero and ten also")
    else:
        print(f"{num3} is greater than zero and less than 10")
else:
    print(f"{num3} has another value") 