def get_grade(score):
    if score >= 80:
        return "HD"
    elif score >= 70:
        return "D"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "P"
    else:
        return "fail"

students = [] 
scores = []

while True:
    name = input(" students name (done to finish)= ")
    if name == "done":
        break
    score = int(input("marks="))
    students.append(name)
    scores.append(score)
print("\n===== Results =====")
for i in range(len(students)):
    grade = get_grade(scores[i])
    print(students[i], "-", scores[i], "-", grade)

print("\naverage:", round(sum(scores)/len(scores), 1))
print("highest mark:", max(scores))
print("lowest mark:", min(scores))
