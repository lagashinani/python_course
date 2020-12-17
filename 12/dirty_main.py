import datetime

from application.salary import *
from application.people import *

if __name__ == '__main__':
    print("Current date = ", datetime.date.today().strftime("%d-%m-%Y"))
    print(calculate_salary())
    print()
    print(get_employees())
