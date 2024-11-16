
percentage = float(input("Enter your percentage: "))

if 85 <= percentage <= 100:
    grade = "A+"
elif 70 <= percentage <= 84:
    grade = "A"
elif 65 <= percentage <= 69:
    grade = "A-"
elif 60 <= percentage <= 64:
    grade = "B+"
elif 55 <= percentage <= 59:
    grade = "B"
elif 50 <= percentage <= 54:
    grade = "B-"
elif 45 <= percentage <= 49:
    grade = "C+"
elif 40 <= percentage <= 44:
    grade = "C"
elif 35 <= percentage <= 39:
    grade = "C-"
elif 30 <= percentage <= 34:
    grade = "D+"
elif 25 <= percentage <= 29:
    grade = "D"
else:
    grade = "E"

print(f"Your grade is: {grade}")