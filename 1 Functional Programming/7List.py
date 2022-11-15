# LIST IS MUTABLE, WE CAN CHANGE OR UPDATE THESE VALUES...
nums = [10,20,30,40,50,60,70]

print(nums)
print(nums[0], nums[1])
print(nums[-1], nums[-5])
print(nums[2:])

#print(nums[100])  IT WILL SHOW ERROR BCOZ WE ARE ACCESSING OUT OF RANGE VALUE

nums.append(80)
print(nums)
nums1 = nums.copy()
print(nums1)
nums.extend([90,100,110])
print(nums)
nums.insert(0, 0)
print(nums)
nums.remove(0)
print(nums)
nums.pop()
print(nums)
print(nums.count(10))
print(nums.index(50))
print(min(nums), max(nums), sum(nums))

names = ['Navin', 'Kiran', 'John']
values = [9.5, 'Navin', 25]
newlist = [names, values]
print(newlist)