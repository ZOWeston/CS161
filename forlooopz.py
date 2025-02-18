#1.)
lowernum = input("Enter the lower number: ")
highernum = input("Enter the higher number: ")
lowernum = int(lowernum)
highernum = int(highernum)  #conversion to int
numresult = "The even numbers of " + str(lowernum) + " to " + str(highernum) + " are: " #setup for string var
for num in range(lowernum, (highernum + 1)):
    if num % 2 == 0:    #if number is divisible by two
        numresult = numresult + str(num) + ", " #add it to the list
print(numresult)

#2.)
enterint = input("Enter a positive integer: ")  
enterint = int(enterint) 
breakez = False #while loop breakout
crazyintWOW = 1 #number that input gets MOD'd by
swagresult = "The integers that are factors of " + str(enterint) + " are: "
while breakez == False:
    int2 = enterint % crazyintWOW
    if int2 == 0:   #if input is divisible by int
        swagresult = swagresult + str(crazyintWOW) + ", " #add it to the list
    crazyintWOW = crazyintWOW + 1
    if crazyintWOW == enterint + 1:
        breakez = True
print(swagresult)

#3.)
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
name = input("Enter your last name: ")
name = name.lower() #making it not case sensitive
alphanum = 0    #number in the sequence of the list
alphasum = 0    #sum of the total

for x in name:  #for every entry in input
    alphanum = 0    #reset alphanum to 0
    for y in alphabet:  #for every entry in the alphabet
        if x != y: #if entry in name isnt equal to entry in alphabet
            alphanum = alphanum + 1 #counter in sequence up
        else:
            alphasum = alphasum + alphanum #if it is equal, go to next entry in name
            alphanum = -99  #by far the JANKIEST solution yet but we TAKE THOSE

print(alphasum)

#4.)
squinteger = 1  #square integer variable
def squaresfunc(integer):   
    for dex in range(integer+1): #for entries in the range of input 
        squinteger = dex ** 2 #entry squared
        print(squinteger) #print entry squared

squaresfunc(int(input("Enter an integer: ")))   #making it an input

#5.)
unsorted_list = [12, 43, 22, 34, 2, 21, 3, 33, 81] #from the assignment
odd_list = [] #a list for odd numbers
even_list = [] #a list for even numbers
for x in unsorted_list: #for entry in OG list
    if x % 2 != 0:  #if its not divisible by 2 its odd
        odd_list.append(x)
    else:   #if it is, its even
        even_list.append(x)
odd_list = sorted(odd_list) #using pythons built in sorter
even_list = sorted(even_list, reverse=True) #using pythons built in reverse modifier
for x in even_list: #for entry in even list
    odd_list.append(x) #put the number at the end of odd list

print(odd_list) #this was absolutely not the intended way of doing this 
#but i feel really proud of myself for figuring this out so im keeping it >:)

#6.)
arrangement = [5,6,4,7,3,8,2,9,1,0] #list of random numbers
print(arrangement) #print for reference
breakout = False #breakout for while loops
lennum = len(arrangement) #variable to shorten
recurser = 1 #number to get to end number
recurser2 = 2 #number to get to left of recurser 1
while breakout == False:
    if arrangement[lennum-recurser2] < arrangement[lennum-recurser]: #if the number before the end number is smaller
        storeval1 = arrangement[lennum-recurser2] #swap their places
        storeval2 = arrangement[lennum-recurser]  #^^^
        arrangement[lennum-recurser2] = storeval2 #^^^
        arrangement[lennum-recurser] = storeval1  #^^^
        breakout = True #break the loop; we done
    else: #if the number to the left isnt smaller...
        recurser = recurser + 1 #add to the subtraction variable
        recurser2 = recurser2 + 1 #to go further down the list

print(arrangement)  #now this is some real spaghetti code
                    #but its like 12am to be fair