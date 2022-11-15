# FOR LOOP WITH ELSE---
# A for loop have an option of else block as well, the else part is executed if the items in the sequence used in for loop exhaust. the break statement can be used to stop a for loop, in such case else part would be ignored...

digits = [0,1,3]
for i in digits:
    print(i)
else:
    print("For loop Over")

# But due to unfair output we use for else statement will break keyword to run the else block only when the break keyword was not executed

# WHILE LOOP WITH ELSE ---
# Same as with for loop while loop can also have else block the else part is executed, if the condition in the while loop evaluates to false. the while loop can be terminated with break statement. In such part else part is ignored. Hence a while loop else part runs if no break occurs and the condition is false...

count = 0
while count < 3:
    print(f"Inside Loop under value of {count}")
    count = count + 1
else: 
    print("While loop ever")