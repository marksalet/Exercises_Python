string = "Guido van Rossum heeft programmeertaal Python bedacht."

stringSplit = list(string)
for x in stringSplit:
    if x in 'aeuio':
        print(x, end = '')