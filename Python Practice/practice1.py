#using function

def is_palindrom(str):
    cleaned_str = str.replace(" ", "").lower()
    return cleaned_str == cleaned_str[::-1]

print(is_palindrom("Madam"))
print(is_palindrom("Hello"))


#Splits
def string(str):
    words = str.split()
    print(words)
string("Hello World from Python")

#Join 
def string1(str):
    words = " ".join(str)
    print(words)
string1(["Hello", "world"])


# Replace 
# using print
def replace_substring(s, old_sub, new_sub):
    print(s.replace(old_sub, new_sub))

input_string = "apples are red, apples are sweet"
substring_to_replace = "apples"
replacement = "oranges"
replace_substring(input_string, substring_to_replace, replacement)
# or

# using return
def replace_substring1(s, old_sub, new_sub):
    return s.replace(old_sub, new_sub)

input_string = "apples are red, apples are sweet"
substring_to_replace = "apples"
replacement = "oranges"

output_string = replace_substring1(input_string, substring_to_replace, replacement)
print(output_string)

# try & except
def input(num):
    try:
        sum = int(num)
        print(f"Answer: {sum}")
    except ValueError:
        print("Error: Input is not a valid integer")
    except TypeError:
        print("Error: Input is the wrong type")
    else: 
        print("Processing Completed successfully")
    finally:
        print("End of processing")

input(23)

input("123")

input("abc")

input([1, 2, 3])

