class Employee:
    def __init__(self,eno,ename,esal,eaddr):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr
    def display(self):
        print("empnumber:",self.eno)
        print("ename:",self.ename)
        print("salary:",self.esal)
        print("address:",self.eaddr)

e1=Employee(476,"rizwan",25000,"vijayawada")
e2=Employee(480,"fayaz",259870,"Hyderabad")
e1.display()
e2.display()
