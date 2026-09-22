#Dan Rey Lumiib, Aaron Jr. Delos Reyes, Jairus Galanza
#8-Adelfa
#22/09/2026

print("<=======================>")
print("Student Age Validation")
print("<=======================>")

try:
    age = int(input("Enter the student age: "))
    print("Valid Age")
except ValueError:
    print("Invalid Age, please enter a whole number")

print("<=======================>")
print("Username Validator")
print("<=======================>")

username = input("Enter username")

if 5<= len(username) <= 10 and username.isalnum():
    print("Valid username")
else:
    print("Invalid username")

print("<=======================>")
print("School Grade Level Validator")
print("<=======================>")

valid_grade_level = [7, 8, 9, 10, 11, 12]
grade_level = int(input("Enter grade level"))

if grade_level in valid_grade_level:
    print("Valid grade level")
else:
    print("Invalid grdae level")
