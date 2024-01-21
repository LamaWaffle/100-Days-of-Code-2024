
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0            # To get the average, we need the total.
num_of_students = 0         # To get total number of students.

for height in student_heights:     # item from the list, add detail into total_height var.
    total_height += height
    num_of_students += 1        # here on each loop, i am adding +1.

average = total_height // num_of_students

print(f"Total height = {total_height}")
print(f"number of students = {num_of_students}")
print(f"average height = {average}")
