def calculate_result(marks):
    total = sum(marks)
    average = total / len(marks)
    
    if average >= 75:
        return "Distinction"
    elif average >= 60:
        return "First Class"
    elif average >= 50:
        return "Second Class"
    elif average >= 35:
        return "Third Class"
    else:
        return "Fail"

# Input for student details
student_number = int(input("Enter student number: "))
student_name = input("Enter student name: ")
marks = []

# Input for marks in three subjects
for i in range(3):
    mark = float(input(f"Enter mark in subject {i+1}: "))
    marks.append(mark)

# Calculate total and average marks
total_marks = sum(marks)
average_marks = total_marks / len(marks)

# Determine result
result = calculate_result(marks)

# Print student result
print("\nStudent Result:")
print("Number:", student_number)
print("Name:", student_name)
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)
print("Result:", result)
