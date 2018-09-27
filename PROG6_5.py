def kwadraten_som(grondgetallen):
    antwoord = 0
    for x in grondgetallen:
        if x > 0:
            antwoord += x**2
    return antwoord

print(kwadraten_som([ 4, 5, 3, -81 ]))