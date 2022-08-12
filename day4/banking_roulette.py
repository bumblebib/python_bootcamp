
import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
number = len(names)
random_number = random.randint(0,number-1)
who_pays = names[random_number]

print(f"{who_pays} is going to buy the meal today!")