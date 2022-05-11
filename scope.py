#esta es la declaracion global y se puede ver en todo el programa,
#aunque en las funciones cambia de valor porque la sobreescribe
z = 5

#se ejecuta despues y tambien es local, solo se ve en my_function
def my_func():
    z = 3

    #se ejecuta primero y esta z es local, solo se ve en my_other_function
    def my_other_func():
        z = 2
        print(z)
    
    my_other_func()

    print(z)

my_func()

print(z)