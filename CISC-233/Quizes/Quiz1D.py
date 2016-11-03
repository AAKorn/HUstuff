s =raw_input("Type your string: ")
for char in ["'",".","!","?"]:
    if char in s:
        s=s.replace(char,"") 
print s
