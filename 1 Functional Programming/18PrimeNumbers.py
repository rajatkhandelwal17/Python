a = int(input("Enter Value of number: "))
for i in range(2, a):
    if a % i == 0:
        print("Not Prime Number")
        break
    else:
        print("Prime Number")

########################################################################################

a = int(input("Enter Value of number: "))
flag = 0
for i in range(2, a):
    if a % i == 0:
        flag = 1
        break
if flag == 0: print("Prime Number")
else: print("Not Prime Number")

