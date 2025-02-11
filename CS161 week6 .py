#1.)
usernum1 = input("Enter a number to count down from: ")
try:
     usernum1 = int(usernum1)
except:
    print("Please enter a numeric value")

while usernum1 > 0:
     print(usernum1)
     usernum1 = usernum1 - 1    #this loop prints a number and then makes it one less until it is 0
print("We're leaving ground!")

#2.)
usernum2 = input("Enter a number to count down even or odd: ")
try:
     usernum2 = int(usernum2)
except:
    print("Please enter a numeric value")

while usernum2 > 0:
     usernum3 = usernum2 % 2
     if usernum3 == 0:
        print(str(usernum2) + " is even")       #this loop checks if the number is divisible by two, if so, its even, if not, its odd.
     else:
        print(str(usernum2) + " is odd")
     usernum2 = usernum2 - 1
print("We're leaving ground!")

#3.)
usernum4 = input("enter an integer: ")
decrease = input("enter how much you want to be taken from it: ")

try:
     usernum4 = int(usernum4)
except:
    print("Please enter a numeric value")

try:
     decrease = int(decrease)
except:
    print("Please enter a numeric value")

while usernum4 > 0:
    print(str(usernum4))            #subtracts decrease from usernum4 until usernum4 is less than 0
    usernum4 = usernum4 - decrease

#4.)
userword = ""
length = 5
while length >= 5:
    userword = input("Enter a word: ")
    length = len(userword)
    if length >= 5:
        print(f"{userword} has {length} numbers!")  #finds the length of the inputted word, then prints this statement if its more than 5 characters
if length < 5:
    print("goodbye")

breakout = False    #return of the king
length2 = 5
userword2 = ""
tries = 0
while breakout == False:
    userword2 = input("Enter a word: ")
    length2 = len(userword2)
    if length2 < 5:                                #if the length of the word is less than 5, exit
        breakout = True
    elif tries != 5:
        print(f"{userword2} has {length2} numbers!") #if its more than 5, print this statement and add a try
        tries = tries + 1
    else:
        breakout = True #if tries is maximized, break the loop

if length2 < 5 and tries != 5:
    print("goodbye")
elif tries == 5:
    print("OUT OF TRIES!")

#5.)
dec = 10
binary = 0b1010
hexval = 0xa

while dec != 101:

    print(str(bin(binary)) + " " + str(dec) + " " + str(hex(hexval)))   #saved by these built in translation functions
    dec = dec + 1                                                       #i was about to be up for another couple hours doing it manually
    binary = binary + 0b0001
    hexval = hexval + 0x1

#6.)
def starsrec(stars):    #stars (recursion)
    i = ""              #string variable
    stars2 = 0          #surprise tool that will help us later
    while stars != 0:
        i = i + "*"     #add an * to the string
        stars = stars - 1   #lose a stars until 0
    while stars2 != len(i): #once 0, if stars2 is not equal to the length of i
        print(i[0:len(i)-stars2])   #print length of i - stars2 until 0
        stars2 += 1 #add 1 to stars2
        
starsrec(5)

def starsiter(stars):   #stars (iterable)
    i = ""
    stars2 = 0
    for x in range(stars):  #for entries in the range of stars (in our case 5)
        i = i + "*" #add an * to the i string
    for y in range(stars):  #for entries in the range of stars
        print(i[0:len(i)-stars2]) #print the length of i - stars2 until 0
        stars2 += 1 #stars2 + 1

starsiter(5)