import numpy as np

marks = np.array([75, 80, 65, 90, 88, 72, 95, 60])

print("Marks:", marks)

print("Average:", np.mean(marks))
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))

passed = marks[marks >= 40]

print("Passed Students:", passed)

print("Sorted Marks:", np.sort(marks))