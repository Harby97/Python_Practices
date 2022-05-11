from datetime import datetime

def execution_time(function):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        function(*args, **kwargs)
        final_time = datetime.now()
        time_expended = final_time - initial_time
        print ("pasaron "+ str(time_expended.total_seconds()) + "segundos ")
    return wrapper      


@execution_time
def random_func():
    for i in range (1, 1000000):
        pass


@execution_time
def suma (a: int, b: int):
    return a + b

@execution_time
def saludo(nombre = 'cesar'):
    print ('Hola ' + nombre)

random_func()
suma(3,5)
saludo('Raul')