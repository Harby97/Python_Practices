from datetime import datetime

def headings(function):
    def write_heading(*args, **kwargs):
        initial_time = datetime.now()
        print('el resultado de su calculo fue: ')
        print(function(*args, **kwargs))
        print('Fin del calculo')
        final_time = datetime.now()
        time_expended = final_time - initial_time
        print ("pasaron "+ str(time_expended.total_seconds()) + "segundos ")

    return write_heading


@headings
def addition(a: int, b: int):
    return a+b


@headings
def subtraction(a: int, b: int, c:int, d:int):
    return a-b-c-d

@headings
def multiplication(*args):
    length = len(args)
    accumulator = 1
    for i in range (length):
        accumulator = args[i] * accumulator

    return accumulator


if __name__ == "__main__":
    addition(1,2)
    subtraction(100,2,3,23)
    multiplication(2,2,2,2,2,2,2,2,2,2)