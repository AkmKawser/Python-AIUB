#task-1

class Student:
                 
    def setIdd (self,i):
        self.idd=i        
    def setName (self,n):
        self.name=n
    def setCgpa (self,c):
        self.cgpa=c


    def getIdd(self):
        return self.idd
    def getName(self):
        return self.name
    def getCgpa(self):
        return self.cgpa


s=Student()  #created object using Student() constructor
s.setIdd(15)
s.setName("Kawser")
s.setCgpa(4)

print(s.getIdd())
print(s.getName())
print(s.getCgpa())
    
