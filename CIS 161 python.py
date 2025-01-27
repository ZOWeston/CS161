#1.)
def average(num1, num2, num3):
    '''adds up three numbers and then divides them by 3 to find the average'''
    return(num1 + num2 + num3)/3
print(average(5,7,9))

#2.)
#print(average(5,7,9))
#def average(num1, num2, num3):
#    '''adds up three numbers and then divides them by 3 to find the average'''
#    return(num1 + num2 + num3)/3                                       
#                                       No, this would not run on its own because the variable "average" would not have been defined yet                                        

#3.)
#print(num1) 
#no, this doesnt run because variables defined in functions can only be used in the context of their function
#(you could make the variable global if it was really necessary)

#4.)
def dog_to_human(dog_age):
    '''This converts the dogs age to human years'''
    i = 24 + (dog_age - 2) * 4
    return print(str(dog_age) + " dog years is equal to " + str(i) + " Human years")
dog_to_human(5)

#5.)
def car_calculate(price, years, type):
    '''though they're a little lazy, good ol elif's were good enough for this calculator, larger data structures would require a library.'''
    if type == "German":
        price = (price / 1.05)*years
    elif type == "Japanese":
        price = (price / 1.07)*years
    elif type == "Italian":
        price = (price * 1.05)*years
    print("The value of " + type + " car will be $" + str(price) + " after " + str(years) + " years")

car_calculate(35000,10,"German")
car_calculate(35000,10,"Japanese")
car_calculate(35000,10,"Italian")

#6.)
dog_name = input("What is your dogs name?: ")
dog_age = input("what is your dogs age in years?: ")

def dog_to_human2():
    '''This converts the dogs age to human years'''
    i = 24 + (float(dog_age) - 2) * 4
    return print("your " + str(dog_name) + " is " + str(i) + " human years old")
dog_to_human2()

#7.)
scoops = input("How many scoops would you like?: ")

def price():
    '''this just does the calculations, gotta make sure its a float though'''
    price = (float(scoops) * 1.15 + 2.25)
    print("That'll be $" + str(price))
price()
