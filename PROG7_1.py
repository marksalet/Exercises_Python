def convert(celcius):
    fahrenheit = (celcius * 1.8) + 32
    return fahrenheit

def table():
    print('%-15s %s' % ("F", "C"))
    for c in range(-30, 41, 10):
        print('%-15s %s'% (convert(c), c))

table()
