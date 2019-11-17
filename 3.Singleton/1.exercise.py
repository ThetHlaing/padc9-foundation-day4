
class Config:
 
    someval = 'default value'

    def __init__(self):
        print("This class's instance should only exist once")

s1 = Config()
s1.someval = 'updated value'
print(s1.someval)

s2 = Config()
print(s2.someval)  # updated value
