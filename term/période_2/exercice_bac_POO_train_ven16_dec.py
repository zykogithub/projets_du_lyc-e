class Wagon:
    def __init__(self, contenu):
        "Constructeur"
        self.contenu = contenu
        self.suivant = None

    def __repr__(self):
        "Affichage dans la console"
        return f'Wagon de {self.contenu}'

    def __str__(self):
        "Conversion en string"
        return self.__repr__()


class Train:
    def __init__(self):
        "Constructeur"
        self.premier = None
        self.nb_wagons = int

    def est_vide(self):
        """renvoie True si ce train est vide (ne comporte aucun wagon),
        False sinon
        """
        return self.nb_wagons==None

    def donne_nb_wagons(self):
        "Renvoie le nombre de wagons de ce train"
        return len(self.nb_wagons)

    def transporte_du(self, contenu):
        """Détermine si ce train transporte du {contenu} (une chaine de caractères).
        Renvoie True si c'est le cas, False sinon
        """
        wagon = self.premier
        while wagon is not None:
            if wagon.contenu == contenu:
                return True
            wagon= wagon.suivan
        return False

    def ajoute_wagon(self, nouveau):
        """Ajoute un wagon à la fin de ce train.
        L'argument est le wagon à ajouter
        """
        if self.est_vide():
            self.premier = nouveau
        else:
            wagon = self.premier
            while nouveau.suivant is not None:
                wagon = wagon.suivant
            wagon.suivant = nouveau
        self.nb_wagons = wagon.donne_nb_wagons()

    def supprime_wagon_de(self, contenu):
        """Supprime le premier wagon de {contenu}
        Renvoie False si ce train ne contient pas de {contenu},
        True si la suppression est effectuée
        """
        if self.est_vide():
            return False

        if self.premier.contenu == contenu:
            self.premier = self.premier.contenu
        else:
            precedent = self.premier
            wagon = precedent.suivant
            while wagon.contenu != contenu:
                precedent = self.premier
                wagon = wagon.suivant
                if wagon is None: # pas de "contenu" dans le train
                    return False
            precedent.suivant = wagon.suivant

        # MAJ du nombre de wagons et résultat de la fonction
        self.nb_wagons = wagon.donne_nb_wagons()
        return True

    def __repr__(self):
        "Affichage dans la console"
        contenus_wagons = ['']
        wagon = self.premier
        while wagon is not None:
            contenus_wagons.append(str(wagon))
            wagon = wagon.suivant
        return "Locomotive" + " - ".join(contenus_wagons)

    def __str__(self):
        "Conversion en string"
        return self.__repr__()


# Tests
train = Train()
w1 = Wagon("blé")
train.ajoute_wagon(w1)
w2 = Wagon("riz")
train.ajoute_wagon(w2)
train.ajoute_wagon(Wagon("sable"))
assert str(train) == 'Locomotive - Wagon de blé - Wagon de riz - Wagon de sable'
assert not train.est_vide()
assert train.donne_nb_wagons() == 3
assert train.transporte_du('blé')
assert not train.transporte_du('matériel')
assert train.supprime_wagon_de('riz')
assert str(train) == 'Locomotive - Wagon de blé - Wagon de sable'
assert not train.supprime_wagon_de('riz')
w1 = Wagon('blé')
train.ajoute_wagon(w1)
w2 = Wagon('riz')
train.ajoute_wagon(w2)
train.ajoute_wagon(Wagon('sable'))
train
train.est_vide()
train.donne_nb_wagons()
train.transporte_du('blé')
train.transporte_du('matériel')
train.supprime_wagon_de('riz')
train
train.supprime_wagon_de('riz')
