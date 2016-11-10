import random

nums = [random.randrange(0,1000) for x in range(10000)]

def bubbleSorting(nums):

    Sorted = False
    Limit = len(nums)

    print nums
    while Sorted == False:
        count = 1   


        for x in range(Limit):
            
            
            if 0 <= x + 1 < Limit:

                if nums[x] > nums[x+1]:
                    first, second = x, x+1
                    
                    nums[second], nums[first] = nums[first], nums[second]

                else:
                    count = count + 1
                
                if count == Limit:
                    Sorted = True

        Limit = Limit - 1 

    return nums

print bubbleSorting(nums)
