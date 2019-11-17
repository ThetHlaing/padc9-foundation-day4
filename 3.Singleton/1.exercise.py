
class Config:

    __currentInstance = None
    someval = 'default value'

    @staticmethod
    def getInstance():
        if(Config.__currentInstance is None):
            Config()
        return Config.__currentInstance

    def __init__(self):
        if Config.__currentInstance != None:
            #print("Error here")
            raise Exception("This class is singleton")
        else:
            Config.__currentInstance = self


s1 = Config.getInstance()
s1.someval = 'updated value'
print(s1.someval)

s2 = Config.getInstance()
print(s2.someval)  # updated value
