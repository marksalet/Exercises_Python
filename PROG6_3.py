def lang_genoeg(lengte):
    if lengte >= 120:
        return "Je bent lang genoeg voor de attractie!"
    else:
        return "Sorry, je bent te klein!"

lengte = int(input("Wat is je lengte in mm:"))

print(lang_genoeg(lengte))