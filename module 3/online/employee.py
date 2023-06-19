employees = [
    {
     'name': 'Danil',
     'salary': 200_000
    },
    {
     'name': 'Ilya',
     'salary': 30_000
    },
    {
     'name': 'Nastya',
     'salary': 300_000
    }
]


for emp_ind in range(len(employees)):
    if employees[emp_ind]['name'] == 'Ilya':
        del employees[emp_ind]
        break
for employee in employees:
    print(f"У работника {employee['name']} зарплата в месяц - {employee['salary']}р.")
    print(f"Таким образом, {employee['name']} зарабатывает {employee['salary'] * 12}р. в год")
