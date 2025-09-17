class stud:
    def __init__(self,a,b,c):
        self.sno=a
        self.name=b
        self.age=c
    def disp(self):
            print(self.sno,self.name,self.age)


ob=stud(123,'abc',20)
ob.disp()
