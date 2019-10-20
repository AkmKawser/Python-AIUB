#task-1

class Student:
                 
    def setIdd (self,i):
        idd=i        
    def setName (self,n):
        name=n
    def setCgpa (self,c):
        cgpa=c


    def getIdd(self):
        return idd
    def getName(self):
        return name
    def getCgpa(self):
        return cgpa


s=Student()  #created object using Student() constructor
s.setIdd(15)
s.setName("Kawser")
s.setCgpa(4)

print(s.getIdd)
print(s.getName)
print(s.getCgpa)
    
