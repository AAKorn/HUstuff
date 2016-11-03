import random
message = "Hello, my name is Alexander Korn. The ladies call me bigchiefmaiz. What is yours?"

shift = random.randrange(1,26)

if len(message) >= 64:
    encryptedList = [chr(ord(x)+shift) for x in message]
    encryptedMessage = ''.join(encryptedList)
    print encryptedMessage

