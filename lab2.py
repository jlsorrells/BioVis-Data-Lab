#attribute names
NAMES = ["animal name","hair","feathers","eggs","milk","airborne","aquatic",
         "predator","toothed","backbone","breathes","venomous","fins","legs",
         "tail","domestic","catsize","type"]
TYPES = ["String","Boolean","Boolean","Boolean","Boolean","Boolean","Boolean",
         "Boolean","Boolean","Boolean","Boolean","Boolean","Boolean","Numeric",
         "Boolean","Boolean","Boolean","Numeric"]

def myPrint(i, string):
    if i == len(TYPES) - 1:
        #print(string)
        output.write(string + "\n")
    else:
        #print(string, end=",")
        output.write(string + ",")

#open the output file
output = open("zoo.csv", "w")

#print out the category names
for i in range(len(NAMES)):
    myPrint(i, NAMES[i])

#read the data file
data = open("zoo.data", "r")

#print out the data
for line in data:
    #remvoe newline char
    line = line.strip("\n")
    #split on commas
    values = line.split(",")

    #print each value in the appropriate format
    for i in range(len(values)):
        if TYPES[i] == "Boolean":
            if values[i] == "0":
                myPrint(i, "True")
            elif values[i] == "1":
                myPrint(i, "False")
            else:
                #a boolean value was not 0 or 1
                myPrint(i, "Unknown")
        elif TYPES[i] == "String" or TYPES[i] == "Numeric":
            myPrint(i, values[i])
        else:
            #type was not Boolean, Numeric, or String
            myPrint(i, "Unknown")

#close the output file
output.close()
