# f-string

name = "Santhosh"
age = 19

print(f"My name is {name}. My age is {age}" )

# .format
formated_str = "My name is {}. My age is {}".format(name, age)
print(formated_str)


# list comprehension
# in integer
arr = [2, 1, 6, 3, 9]
odd = [i if i%2 != 0 else "Not oddNumber" for i in arr]
print(odd)

#in string
str_list = ["Santhosh", "Krishna", "Kottai"]
even = [i for i in str_list if len(i)%2 != 0 ]
print(even)
