def som(getallenLijst):
    antwoord = 0
    for x in getallenLijst:
        antwoord = antwoord + x
    return antwoord


print(som([3, 2, 4]))