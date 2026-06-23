import random

students = []

# Generate marks for 40 students
for i in range(1, 41):
    marks = random.randint(35, 100)
    students.append(marks)

# Add 2–3 intentional errors
students[5] = -10        # Invalid negative marks
students[15] = 120       # Marks above 100
students[25] = "Absent"  # Wrong data type

# Display result
print("Student Metrics (Marks):\n")

for i in range(40):
    print(f"Student {i+1}: {students[i]}")
