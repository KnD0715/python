class Person:
    @staticmethod
    def getGender():
        return "Unknown"

class Male(Person):
    @staticmethod
    def getGender():
        return 'Male'

class Female(Person):
    @staticmethod
    def getGender():
        return 'Female'

print(Male.getGender())
print(Female.getGender())