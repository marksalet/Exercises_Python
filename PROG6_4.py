def new_password(oldpassword, newpassword):
    if oldpassword != newpassword and len(newpassword) >= 6:
        return newpassword
    else:
        return "Nieuw wachtwoord is niet goed."

oldpassword = "password123"
newpassword = str(input("Nieuw wachtwoord:"))

print(new_password(oldpassword, newpassword))