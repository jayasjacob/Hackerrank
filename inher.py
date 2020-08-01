class Dog:
    def __init__(self,fname,lname,breed):
        self.firstname = fname
        self.lastname  = lname
        self.breeder   = breed

    def printdog(self):
        print(self.firstname,self.lastname,self.breeder)

class person(Dog):
    def __init__(self, fname, lname, breed):
        super().__init__(fname, lname, breed)
    
x  = Dog('TOM','hr','pomer')
x.printdog()