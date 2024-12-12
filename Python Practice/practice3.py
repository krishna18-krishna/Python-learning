# slicing
def slicing_string(str):
    a = (str[0:5])
    b = (str[0:10:2])
    c = (str[::-1])
    print(a)
    print(b)
    print(c)

slicing_string("Hello world")

# adding
def adding_strings(str1 , str2):
    a = str1 + str2
    
    print(a)

adding_strings("Hello ", "World")

# removing
def removing(str):
    str.remove("Krishna")
    print(str)

removing({"Gokul", "Krishna", "Karthik", "Santhosh"})

# find 
def findString(str):
    str1 = "Santhosh"
    print(str.find(str1))

findString("His name is Santhosh")

# strip
def findString(str):
    print(str.strip())
    print(str.rstrip())
    print(str.lstrip())

findString("       His name is Santhosh      ")

import practice1

print(practice1)