
import csv

with open('data/employee.csv', newline='') as file:
    data = csv.DictReader(file)

    for row_number, row in enumerate(data, start=2):
        employee_id = row['id']
        salary = row['salary']

        if not employee_id:
            raise ValueError("Employee ID is missing in row")
        if float(salary) < 0:
            raise ValueError("Salary is negative in row")
            
    print('validation successful')