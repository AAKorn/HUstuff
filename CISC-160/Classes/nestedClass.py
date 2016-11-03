class student:

    class __info:
        def __init__(self, name, phoneNumber):
            self.n = name
            self.p = phoneNumber

    def __init__(self, id, name, phoneNumber):
        self.i = id
        self.inf = self.__info(name, phoneNumber)
        self.name = name

s = student(6765, "John", 7174567876)

print s.inf

print s.name
