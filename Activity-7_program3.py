
print("<=======================>")
print("School Grade Level Validator")
print("<=======================>")

valid_grade_level = [7, 8 , 9, 10, 11, 12]
grade_level = int(input("Enter grade level"))

if grade_level in valid_grade_level:
    print("Valid grade level: ")
else:
    print("Invalid grade level")