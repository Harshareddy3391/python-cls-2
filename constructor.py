#constructor is a special method and it creates a object instance and it will excutes automatically but only once is called constructor.to create a constructor by using "__init__" key word.

class con:
    def __init__(self,u):
        print("hello i am constructor",u)

a=con(300)

