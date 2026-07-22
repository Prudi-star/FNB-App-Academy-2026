# A student grade classifier

# Name and Marks collection

name = input('Enter your name: ')

# Subject input and marks collection
subject_A =(input('Enter your first subject: '))
markA = float(input(f'Enter {subject_A} mark: '))
subject_B =(input('Enter your second subject: '))
markB = float(input(f'Enter {subject_B} mark: '))
subject_C =(input('Enter your third subject: '))
markC = float(input(f'Enter {subject_C} mark: '))

# Calculate the subjects
marks = (markA + markB + markC) / 3
print(f"Avarage marks: {marks}")

# Assign Pass status
if marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

# Pass status
if marks >= 50:
    status = "PASS"
else:
    status = "FAIL"

# Flag any individual subject mark below 40
intervention = []
if markA < 40:
    intervention.append(subject_A)
if markB < 40:
    intervention.append(subject_B)
if markC < 40:
    intervention.append(subject_C)

# Report card display
print("\n--- Report Card ---")
print(f"Name: {name}")
print(f"Subject A: {subject_A}")
print(f"Subject B: {subject_B}")
print(f"Subject C: {subject_C}")
print(f"Avarage: {marks}")
print(f"Grade: {grade}")
print(f"Status: {status}")

if intervention:
    print("Needs Intervention in:" + ",".join(intervention))
else:
    print("No Intervention Needed")
