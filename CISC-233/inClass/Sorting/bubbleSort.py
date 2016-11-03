import random

nums = [random.randrange(0,1000) for x in range(1000)]

def bubbleSorting(nums):

    Sorted = False
    Limit = len(nums)

    passNum = 0

    print nums
    while Sorted == False:
        count = 1    
        passNum = passNum +1 
        print passNum

        for x in range(len(nums)):

            if 0 <= x + 1 < Limit:
                if nums[x] > nums[x+1]:
                    first, second = x, x+1
                    
                    nums[second], nums[first] = nums[first], nums[second]

                else:
                    count = count + 1
                
                if count == len(nums):
                        Sorted = True

    return nums

print bubbleSorting(nums)
