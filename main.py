marks = [75, 82, 91, 68, 85, 79, 95, 72]

total = sum(marks)
average = total / len(marks)

highest = max(marks)
lowest = min(marks)

passed = 0
failed = 0

for mark in marks:
    if mark >= 40:
        passed += 1
    else:
        failed += 1

print("STUDENT PERFORMANCE REPORT")

print("--------------------------")

print("Total students:", len(marks))

print("Average marks:", average)

print("Highest marks:", highest)

print("Lowest marks:", lowest)

print("Passed:", passed)

print("Failed:", failed)