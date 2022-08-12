# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#combine both strings into one
validation = name1 + name2

#turn into lower case
validation.lower()

#create counting variables
total_true = 0
total_love = 0

#check for counting
for letter in validation:
    for x in "true":
        total_true += letter.count(x)
    for y in "love":
        total_love += letter.count(y)

#combine the numbers into a score
score = int(str(total_true)+str(total_love))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else: 
    print(f"Your score is {score}.")