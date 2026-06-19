import pandas as pd
import numpy as np

num_rows = 200

np.random.seed(42)
hours = np.random.randint(1, 11, size=num_rows)
attendance = np.random.randint(50, 101, size=num_rows)
assignments = np.random.randint(1, 11, size=num_rows)
previous_marks = np.random.randint(30, 101, size=num_rows)

result = []
for h, a, ass, pm in zip(hours, attendance, assignments, previous_marks):
    score = 0.4*h + 0.2*(a/10) + 0.2*ass + 0.2*(pm/10)
    if score >= 7:
        result.append(1)
    else:
        result.append(0)

df = pd.DataFrame({
    'hours': hours,
    'attendance': attendance,
    'assignments': assignments,
    'previous_marks': previous_marks,
    'result': result
})

df.to_csv('student_data.csv', index=False)
print("student_data.csv generated with", num_rows, "rows!")