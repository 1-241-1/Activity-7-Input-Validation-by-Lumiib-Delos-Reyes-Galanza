print("<=======================>")
print("Student Age Validation")
print("<=======================>")

try:
    age = int(input("Enter the student age: "))
    if 12 <= len(age) <= 18:
        print("Valid Age")
    else:
        print("Too Old")
except ValueError:
    print("Invalid Age, please enter a whole number")