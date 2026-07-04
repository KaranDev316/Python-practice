
employee_records = [
    {"role": "developer", "salary": 25_000},
    {"role": "HR", "salary": 20_000},
    {"role": "Finance", "salary": 35_000},
]

for record in employee_records:
   if record["role"] == "developer":
      bonus = 25_000 * 0.1
      record["salary"] += bonus
      print(record)
