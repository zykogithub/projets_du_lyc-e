def mode(heure) :
    assert (heure >= 0 and heure< 24)
    if heure < 9 :
        mode = "Eco"
    elif heure < 22 :
        mode = "Confort"
    else :
        mode = "Erreur"
    return mode

assert mode(3)=="Eco"
assert mode(7.5) == "Eco"

h=float(input("heure : "))

print(mode(h))

#################################################
#################################################
#################################################
#################################################

def semaine(heure, jour) :
    if jour=="lundi" or jour=="mardi" or jour=="mercredi" or jour=="jeudi" or jour=="vendredi" :
        if 6<=lundi<=9 or 17<=lundi<=22 :
            semaine = "confort"
    else :
        semaine = "eco"

    elif jour=="samedi" or "dimanche" :
        if heure 9<=heure<=22 :
            mode="confort"
        else :
            mode : "Eco"

return mode