paspoort = input("Heb je een Nederlands paspoort? Ja/Nee")
leeftijd = int(input("Wat is je leeftijd:"))

paspoort = paspoort.lower()

if leeftijd >= 18 and paspoort == "ja":
    print("Gefeliciteerd, je mag stemmen!")
else:
    print("Sorry, maar je mag nog niet stemmen")