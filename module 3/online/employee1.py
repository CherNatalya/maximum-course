class Employee:
    def __init__(self, name, salary, on_vacation, is_good):
        self.__name = name
        self.__salary = salary
        self.__on_vacation = on_vacation
        self.__is_good_employee = is_good

    def get_info(self):
        return {'name': self.__name, 'salary': self.__salary, 'on_vacation': self.__on_vacation,
                'is_good': self.__is_good_employee}


employees = [Employee('Danil', 200_000, False, True), Employee('Ilya', 30_000, False, True),
             Employee('Nastya', 300_000, True, True), Employee('Andrey', 150_000, False, True),
             Employee('Natalya', 450_000, True, False)]
for emp_ind in range(len(employees)):
    if not employees[emp_ind].get_info().get('is_good'):
        del employees[emp_ind]
        break
for employee in employees:
    print(employee.get_info())
