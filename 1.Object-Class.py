#task-1

class Student:
                 
    def setId (self,i):
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
    
