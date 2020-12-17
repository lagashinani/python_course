import datetime
def logger_decorator_1(function_to_decorate):
    def wrapper():
        filename = "log.log"
        with open(filename, "a") as out:
            print("[1] " + str(datetime.datetime.now()), file=out)
        return function_to_decorate()

    return wrapper

# функция, которая возвращает декоратор, в котором уже прописана переменная, переданная как аргумент
def logger_decorator_func(path_to_log): 
    # сам декоратор, то есть функция, возвращающая нашу функцию, обернутую в обертку
    def logger_decorator_2(function_to_decorate):
        def wrapper():
            filename = path_to_log
            with open(filename, "a") as out:
                print("[2] " + str(datetime.datetime.now()), file=out)
            return function_to_decorate()
        return wrapper
    return logger_decorator_2

@logger_decorator_1
def test_call():
    print("FUNC CALL " + str(datetime.datetime.now()))

test_call()

@logger_decorator_func("log.txt")
def test_call():
    print("FUNC CALL ARG " + str(datetime.datetime.now()))

test_call()

# импортируем модуль people из 12 задания, лежащего рядом
import sys
sys.path.append("../12/application")
import people

# декорируем и вызываемфункцию get_employees
new_people = logger_decorator_func("log.csv")(people.get_employees)
print(new_people())
