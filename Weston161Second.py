#1--------------
x = 25
print(x, bin(x), hex(x))
#---------------

#2--------------

# x = 1.8
# print(x, bin(x), hex(x))

#this gives a TypeError, where in this case we put a float value in a field where only integers are accepted

x = 18
#---------------

#3--------------
y = 0b1000
z = 0xA3
print(y, z)
#---------------

#i think #4 on the homework is a duplicate? thats why it isnt here lol

#5--------------
w = x + y + z
print("The sum is ", w)

#---------------


#Compression
original_size = 300
dictionary_size = 45
compressed_size = 150

compression_percent = 1 - (compressed_size + dictionary_size) / original_size

print("Dictionary Size: ", str(dictionary_size), " characters")
print("Compressed Size: ", str(compressed_size), " characters")
print("Original Size: ", str(original_size), " characters")
print("Compression Percent: ", str(compression_percent * 100),"%")
print("Total: ", str(dictionary_size + compressed_size), " characters")

#------------------------------------------------------------

#extra cred (thats slang for credit im just using slang guys)

negative = ""
ones = ""
twos = ""
fours = ""
eights = ""
sixteens = ""
thirtytwos = ""
sixtyfours = ""

usernum = input("enter a whole number inbetween -127 and 127: ")

try:
    usernum = (int(usernum))
except:
    print("well now thats just being silly")

if usernum > 127 or usernum < -127:
    print("well now thats just being silly")

if usernum >= 0:
    negative = "0"
else:
    negative = "1"
    usernum = abs(usernum)  # we just check if its negative and then calulate it positive with the negative switch on :)

if usernum >= 64:
    usernum = usernum - 64
    sixtyfours = "1"
else:
    sixtyfours = "0"

if usernum >= 32:
    usernum = usernum - 32
    thirtytwos = "1"
else:
    thirtytwos = "0"

if usernum >= 16:
    usernum = usernum - 16
    sixteens = "1"
else:
    sixteens = "0"

if usernum >= 8:
    usernum = usernum - 8
    eights = "1"
else:
    eights = "0"

if usernum >= 4:
    usernum = usernum - 4
    fours = "1"
else:
    fours = "0"

if usernum >= 2:
    usernum = usernum - 2
    twos = "1"
else:
    twos = "0"

if usernum >= 1:
    usernum = usernum - 1
    ones = "1"
else:
    ones = "0"


print(negative,sixtyfours,thirtytwos,sixteens,eights,fours,twos,ones)
