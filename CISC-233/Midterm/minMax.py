import random

nums = [random.randrange(0,100) for x in range(10)]

print nums

largestNum = None
smallestNum = 101
counter = -1


def minMax(nums, counter, largestNum, smallestNum):
    counter = counter + 1
    if counter  == len(nums):
        print smallestNum
        print largestNum
        return
    
    if nums[counter] >= largestNum:
        largestNum = nums[counter]

    if nums[counter] <= smallestNum:
        smallestNum = nums[counter]

    minMax(nums, counter, largestNum, smallestNum)

minMax(nums, counter, largestNum, smallestNum)
