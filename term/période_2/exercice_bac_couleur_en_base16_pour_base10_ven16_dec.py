HEX_DEC = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
            '9':9, 'A':10, 'B':11, 'C':12, 'D':13,'E':14,'F':15
}

def hex_int(seizaine, unite):
    nombre_decimal=HEX_DEC[seizaine]*16+HEX_DEC[unite]
    return nombre_decimal

def html_vers_rvb(html):
    for i in range(1,len(html)-1):
            r=hex_int(html[i], html[i+1])
            v=hex_int(html[i+2], html[i+3])
            b=hex_int(html[i+4], html[i+5])
            return r,v,b
    


# test

assert hex_int('B', '5') == 181, "Échec hex_int exemple 1 de l'énoncé"
assert hex_int('0', '0') == 0, "Échec hex_int exemple 2 de l'énoncé"

assert html_vers_rvb("#C0392B") == (192, 57, 43), "Échec html_vers_rvb exemple 1"
assert html_vers_rvb("#00FF00") == (0, 255, 0), "Échec html_vers_rvb exemple 2"
assert html_vers_rvb("#000000") == (0, 0, 0), 'Échec html_vers_rvb exemple 3'



