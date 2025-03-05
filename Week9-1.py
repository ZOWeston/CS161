#1.)
class Student:
    def __init__(self, first, age, grade):  #Parameters
        self.first = first  #first name
        self.age = age  #student age
        self.grade = grade  #student grade

stn_1 = Student("Raj",16,"11th") #Raj is 16 and in 11th grade
stn_2 = Student("Joe",17,"11th") #Joe is 17 and in 11th grade

print(stn_1.first)
print(stn_1.age)
print(stn_1.grade)

print(stn_2.first)
print(stn_2.age)
print(stn_2.grade)

#2.)
class Staff:
    def __init__(self, name, dep, role, salary):
        self.name = name
        self.dep = dep
        self.role = role
        self.salary = salary
class Teacher(Staff): #child class, calls a previous class's parameters within its own
    def __init__(self, name, dep, role, salary, age): #same params
        super().__init__(name, dep, role, salary) #the super() function makes child inherit all methods and properties from parent 
        self.age = age #added param

stf_1 = Teacher("George", "Science", "Teacher", 70000, 26)
stf_2 = Teacher("James", "Computer Science", "Teacher", 2000000000, 200) #I guessed on a few of these params :P
print(stf_1.name)
print(stf_1.dep)
print(stf_1.role)
print(stf_1.age)

print(stf_2.name)
print(stf_2.dep)
print(stf_2.role)
print(stf_2.age)

#3.)

class Square:
    def __init__(self, length):
        self.length = length
    def area(length): #calls length from earlier
        area = length * length #area of square is side^2
        return "the area of " + str(length) + " is " + str(area) + "!"
    def perimeter(length):
        perimeter = length * 4 #perimeter of square is length*4
        return "the perimeter of " + str(length) + " is " + str(perimeter) + "!"

print(Square.perimeter(100))
print(Square.area(100))