import random

nums = [random.randrange(0,100) for x in range(10)]

nums.sort()

Min = nums[0]
Max = nums[len(nums)-1]

print nums
print Min
print Max
