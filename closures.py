from __future__ import division


def make_repeater(repetition :int):
    def repeater (string :str):
        assert type(string) == str ,'Cuidado solo puedes utilizar una cadena'
        return string*repetition
    
    return repeater


def make_division_by(denominator :int):
    def division(numerator :int):
        return numerator/denominator
    return division



def run():
    word_4_times = make_repeater(4)
    word_10_times = make_repeater(10)
    word_19_times = make_repeater(19)

    print(word_4_times("hello "))
    print(word_10_times("wow "))
    print(word_19_times("math "))

    #reto
    division_by_3 = make_division_by(3)
    print(division_by_3(18))

    division_by_5 = make_division_by(5)
    print(division_by_5(100))

    division_by_18 = make_division_by(18)
    print(division_by_18(54))
    

if __name__ == "__main__":
    run()