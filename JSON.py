import json 

file = open("students.json")
data = json.load(file)
print(data)

for student in data["Students"]:
    print(f"{student['FirstName']} {student['LastName']}")

#KOMANDAS UZDEVUMS 1
#Atrodi vidējo studentu vecumu (Age)

count = 0
total_age = 0
for student in data["Students"]:
    total_age += int(student["Age"])
    count += 1
print(f"Average age: {total_age/count}")
count_female = 0
count_male = 0

total_age_female = 0
total_age_male = 0
total_grade_female = 0
total_grade_male = 0

for student in data["Students"]:
    if student["Gender"] == "Female":
        count_female += 1
        total_age_female += int(student["Age"])
        total_grade_female += int(student["Grade"])
    elif student["Gender"] == "Male":
        count_male += 1
        total_age_male += int(student["Age"])
        total_grade_male += int(student["Grade"])

print(f"Female average age: {total_age_female/count_female}")
print(f"Female average grade: {total_grade_female/count_female}")
print(f"Male average age: {total_age_male/count_male}")
print(f"Male average grade: {total_grade_male/count_male}")