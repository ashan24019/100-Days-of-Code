student_scores = input("Inpur a list of students scores:").split()

for n in range(0 , len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

Highest_score = 0

for score in student_scores:
    if score > Highest_score:
        Highest_score = score
    
print(f"The highest score in the class is:{Highest_score}")
          