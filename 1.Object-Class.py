#QUESTION-1
#Write a class Student that has the following attributes:
# int id
# String name
# double cgpa
#There is a set method and a get method for each of the attributes. There is also a main method
#in this class. Inside the main method create one object of the Student class and demonstrate
#all the methods.



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
    
