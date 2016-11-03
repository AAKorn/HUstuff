n = int(raw_input("What is n?: "))
nums = []

if n > 0:
    n2 = (2*n)+1
else:
    print "n must be a positive integer"

for x in xrange(0,n2):
    if x % 2 == 0:
        nums.append(x)
print sum(nums)
