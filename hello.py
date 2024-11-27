a = int(input("enter mark1: "))
b = int(input("enter mark2: "))
avg = (a+b)/2;
if avg>=80:
    print("Grade: A")
elif avg>=70 and avg<80:
    print("Grade: B")
elif avg>=60 and avg<70:
    print("Grade: C")
elif avg>=50 and avg<60:
    print("Grade: D")
else:
    print("Grade: E")

