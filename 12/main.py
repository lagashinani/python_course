import datetime

# 2 разных способа импорта
import application.salary
from application.people import get_employees

if __name__ == '__main__':
    print("Current date = ", datetime.date.today().strftime("%d-%m-%Y"))
    print(application.salary.calculate_salary())
    print()
    print(get_employees())
