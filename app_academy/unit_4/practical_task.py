student_name = input("Enter Student Name: ")
english_mark = float(input("Enter English Mark: "))
math_mark = float(input("Enter Maths Mark: "))
history_mark = float(input("Enter History Mark: "))

average_mark = round((english_mark + math_mark + history_mark) / 3, 2)

if average_mark >= 80:
    letter_grade = "A"
elif average_mark >= 70:
    letter_grade = "B"
elif average_mark >= 60:
    letter_grade = "B"
elif average_mark >= 50:
    letter_grade = "C"
else:
    letter_grade = "F"

print(f"Report card for: {student_name}")
print(f"\t English: \t{english_mark}")
print(f"\t Maths: \t{math_mark}")
print(f"\t History: \t{history_mark}")
print(f"\t Average: \t{average_mark}")
print(f"\t Grade: \t{letter_grade}")

if average_mark >= 50:
    print("\t Stundent Status: Pass")
elif average_mark < 40:
    print("\t Stundent Status: Needs Intervention")
else:
    print("\t Stundent Status: Fail")