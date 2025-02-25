import time #surprise tool to help for later

#1.)
word1 = input("Enter a word: ")

print(word1)

word1 = word1.upper()

word2 = input("Enter the same word in uppercase: ")

if word1 == word2: #== or != work, just swap around the outputs
    print("Stop shouting!")
else:
    print("Thanks for keeping it quiet.")


#2.)
word = input("Enter a string: ")
count = 0
if ('a' in word):
    count = count + 1
if ('e' in word):
    count = count + 1
if ('i' in word):
    count = count + 1
if ('o' in word):
    count = count + 1
if ('u' in word):
    count = count + 1
count2 = count 
count = 0 #reduce reuse recycle
for x in word:
    if ('a' in x):
        count = count + 1
    elif ('e' in x):
        count = count + 1
    elif ('i' in x):
        count = count + 1
    elif ('o' in x):
        count = count + 1
    elif ('u' in x):
        count = count + 1
#if else if else if else if else if else...
print(f"{word} has {count} vowels, {count2} of which are different!")


#3.)
string1 = input("Enter a string: ")
string2 = input("Enter a string: ")

if string1 > string2:
    print(f"{string2} comes before {string1}")
else:
    print(f"{string1} comes before {string2}")


#4.)
breakout = False #classic.
while breakout == False:
    email = input("Please enter your email: ")
    confirmation = input("Please confirm your email: ")
    if email == confirmation:
        breakout = True
    else:
        print("Please try again")
print("Thank you!")


#5.)
start = 0 #reset timer
stop = 0

start = time.perf_counter_ns()
stop =  time.perf_counter_ns()

def iterfactorial(num):
    start
    o=2 #just any number that isnt 1 so the later loop don't break
    i=num
    num2 = num
    for x in range(num): #for every number in num
        if o != 1:  #until o is 1
            o = i - 1 #o is 1 less than i
            num2 = num2 * o
            i = i-1 #remove 1 from i
    stop
    print(str(num) + " factorial is " + str(num2))
    print("it took " + str(stop - start) + " nanoseconds to complete iteravely")

iterfactorial(3)
iterfactorial(10)
iterfactorial(25)

start = 0   #reset timer
stop =  0

start = time.perf_counter_ns()
stop =  time.perf_counter_ns()

def recfactorial(num):
    start   #start timer
    savenum = num   #for later
    var2 = 2    #equivalent to o
    numerodos = num #equivalent to i
    while var2 != 1:
        var2 = numerodos - 1 
        num = num * var2
        numerodos = numerodos - 1
    stop
    print(str(savenum) + " factorial is " + str(num))
    print("it took " + str(stop - start) + " nanoseconds to complete recursively")


recfactorial(3)
recfactorial(10)
recfactorial(25)


#results seem to vary, though it always seems to take longer to do it
#iteravely, which is definitely a first, but its probably something
#to do with the way I wrote it.
#I am newer to for loops after all :P



