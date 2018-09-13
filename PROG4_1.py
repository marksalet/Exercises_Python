cijferPROG = 7.5
cijferICOR = 7
cijferCSN = 6

gemiddelde = round((cijferCSN + cijferICOR + cijferPROG) / 3 ,2)
gemiddeldeTekst = 'Je gemiddelde cijfer is:'

cijfers = cijferPROG + cijferICOR + cijferCSN
kosten = round(cijfers * 30 ,2)
kostenTekst = 'en je krijgt €'
print(gemiddeldeTekst ,gemiddelde ,kostenTekst ,kosten)
