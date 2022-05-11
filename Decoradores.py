def mayusculas (func):
    def envoltura(texto):
        return func(texto).upper()
    return envoltura

@mayusculas
def mensaje(nombre):
    return f'{nombre}, ingeniero mecatronico'

print(mensaje('harby'))