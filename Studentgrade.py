
marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks {i}: "))
    marks.append(mark)

average = sum(marks) / 5


if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
elif average >= 50:
    grade = "E"
else:
    grade = "FAIL"


print("\n--- Result ---")
print(f"Average Marks: {average:.2f}")
print(f"Grade: {grade}")
