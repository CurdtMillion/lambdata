#my_mod.py

def enlarge(n):
    '''
    Multiplies a number by 100

    Param: n (numberic / float / int)

    Return the enlarged number (numeric)
    '''
    return n * 100


if __name__ == "__main__":

    x = 5
    print(enlarge(x))

    y = int(input('Please choose a number (e.g. 5): '))
    print(enlarge(y))
