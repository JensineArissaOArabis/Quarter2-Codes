num_students = int(input("Enter number of students: "))
num_subjects = int(input("Enter number of subjects: "))

total_class = 0
total_scores = 0

for student in range(1, num_students + 1):
    print(f"\nStudent {student}")
    student_total_score = 0
    for subject in range(1, num_subjects + 1):
        score = float(input(f"Enter score {subject}: "))
        student_total_score += score
    
    student_average = student_total_score / num_subjects
    print(f"Average for Student {student} = {student_average:.1f}")
    
    total_class += student_total_score
    total_scores += num_subjects

class_average = total_class / total_scores
print(f"\nClass Average = {class_average:.1f}")