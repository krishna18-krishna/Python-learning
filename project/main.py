print("Welcome to learn with me")

player = input("Do you want to play? ")

if player.lower() != "yes":
    quit()

print("Ok, let's play!")
score = 0 

# Question 1
question = input("1. What is the capital of France? ")
if question.lower() == "paris":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is Paris.")

# Question 2
question = input("2. How many continents are there in the world? ")
if question.isdigit() and int(question) == 7:  # Ensure input is a number
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 7.")

# Question 3
question = input("3. What planet is known as the Red Planet? ")
if question.lower() == "mars":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is Mars.")

# Question 4
question = input("4. What is the chemical symbol for water? ")
if question.lower() == "h2o":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is H2O.")

# Question 5
question = input("5. What is 5 + 3? ")
if question.isdigit() and int(question) == 8:  # Ensure input is a number
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 8.")

# Question 6
question = input("6. What is the square root of 16? ")
if question.isdigit() and int(question) == 4:  # Ensure input is a number
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 4.")

# Final Score
str_in = input("If you want the score? ")
if str_in.lower() == "yes":
    print("Your score is " + str(score))
elif str_in.lower() == "no":
    print("Thankyou for Playing")
