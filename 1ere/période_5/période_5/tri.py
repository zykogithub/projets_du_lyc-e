A=[[2,7,6],
   [9,5,1],
   [4,3,8]
   ]


def diagonal1(liste):
    rr=[]
    for i in range (len(liste)):
        rr.append(liste[i][i])
    qq=rr[0]+rr[1]+rr[2]
    return qq

def diagonal2(liste):
    rr=[]
    for i in range (len(liste)):
        rr.append(liste[i][2-i])
    qq=rr[0]+rr[1]+rr[2]
    return qq


def colonne(liste):
    rr=[]
    tt=[]
    for i in range (len(liste)):
rr[0]+rr[1]+rr[2]        rr.append(liste[i][0])
    for i in range (len(liste)):
        rr.append(liste[i][2])

    qq=rr[0]+rr[1]+rr[2]
    ee=tt[0]+tt[1]+tt[2]
    if qq==ee:
        return True
    else:
        return False


print(colonne(A))
