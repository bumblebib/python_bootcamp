# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
amount_of_students = len(student_heights)
total_height = sum(student_heights)
average_height = total_height / amount_of_students

total = round(average_height)

print(total)
