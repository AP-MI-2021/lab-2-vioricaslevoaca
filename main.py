def is_palimdrome(n):
    ogl = 0
    x = n
    while n != 0:
        c = n % 10
        ogl = ogl * 10 + c
        n = n // 10
    if ogl == x:
        return True
    else:
        return False


def test_is_palindrome():
    assert (is_palimdrome(121) == True)
    assert (is_palimdrome(122) == False)


def get_base_2(n: str):
    rezultat = 0
    putere = 1
    while n != 0:
        rest = n % 2
        rezultat = rezultat + rest * putere
        putere = putere * 10
        n = n // 2
    return rezultat


def test_get_base_2():
    assert (get_base_2(234) == 11101010)


def main():
    while True:
        test_is_palindrome()
        test_get_base_2()
        print('1. Verifica daca un nr e palindrom')
        print('2. Conversie din baza 10 in baza 2')
        print('x. Iesire din program')
        optiune = input('Alege optiunea: ')
        if optiune == '1':
            n = int(input("Dati nr: "))
            print(is_palimdrome(n))
        elif optiune == '2':
            n = int(input("Dati nr: "))
            print(get_base_2(n))

        elif optiune == 'x':
            break


if __name__ == '__main__':
    main()
