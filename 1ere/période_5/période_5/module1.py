# Créé par n.mohamed, le 31/05/2022 en Python
from PIL import Image

source= Image.open('ange.png')

largeur,hauteur= source.size

but = Image.new("RVB",(largeur,hauteur))

for y in range (hauteur) :
    for x in range (largeur) :
        g=source.getpixel(x,y)
        but.getpixel((x,-y),(g))

but.save("rrrr.png")
but.show



