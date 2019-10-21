class Student:
                 
    def setId (self,i):     #for more efficiency we can replace all these set methods with a single parametarized constructor __init__() method.
        self.id=i        
    def setName (self,n):
        self.name=n
    def setCgpa (self,c):
        self.cgpa=c

    def getId(self):
        return self.id
    def getName(self):
        return self.name
    def getCgpa(self):
        return self.cgpa


s=Student()  #created object using Student() constructor
s.setId(15)
s.setName("Kawser")
s.setCgpa(4)

print(s.getId())
print(s.getName())
print(s.getCgpa())
    
