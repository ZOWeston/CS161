user_name = input("Hello, what is your name?: ")
print("Welcome, " + user_name)

user_age = input("please enter your age: ")

try:
    user_age = int(user_age)    
except:
    "please enter a valid number"

print(f"you are currently {user_age}, in five years you will be {user_age + 5}") #user_age + 5 would typically error here because input's are strings by default
                                                                                 #however we fixed this by simply using int() to convert it from a string to an integer

print(f"let's run over this again, you are currently {user_age}")   #after learning them a week or so ago I cannot STOP using f strings, they are so handy
user_addition = input("how many years would you like to add to your age?: ")

try:
    user_addition = int(user_addition)    
except:
    "please enter a valid number"

user_age = user_addition + user_age

user_age = str(user_age) #we dont have to try except because I dont think this one *can* error

print(f"in {user_addition} years, you will be {user_age}")

try:
    user_workhours = float(input("How many hours have you worked this week?: "))
except:
    print("Please enter a valid number.")
    user_workhours = 0  #sorta a failsafe so the program doesnt freak out

try:
    user_wage = float(input("enter your hourly wage, no $ sign: "))
except:
    print("Please enter a valid number.")
    user_wage = 0

week_pay = user_workhours*user_wage
annual_pay = week_pay*52.1429   #just some calculations, leap year makes calender math such a headache

print(f"your gross pay this week is {week_pay}")
print(f"your estimated annual gross pay is {annual_pay}")

#not doing any extra credit this week, sorry! got a ton of math backed up that i gotta do