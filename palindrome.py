import os

#definicion de funciones con tipado estatico
def is_palindrome(word: str) -> bool:
    word = word.replace(' ','').lower()
    return word == word[::-1]


def is_prime(number: int) -> bool:
    list = [x for x in range(2,number) if number % x == 0]
    if (len(list) == 0):
        return True
    else:
        return False

if __name__ == "__main__":
    os.system("cls")
    try:
        numero : int = input('Ingresa un numero por favor: ')
        assert numero.isnumeric() == True and int(numero) > 0, 'el numero ingresado debe ser positivo'
    except AssertionError as AE:
        print('el numero ingresado debe ser positivo')

    print(is_prime(int(numero)))