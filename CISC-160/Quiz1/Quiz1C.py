vowels = ['a', 'e', 'i','o','u']
string = raw_input("Type in a word: ").lower()
count = 0
for x in vowels:
    for e in string:
        if x == e:
            count+=1
print "Number of vowels in string:", count

