import graphviz
from graphviz import Digraph
from graphviz import nohtml

class Node():


    def __init__(self,val : str) -> None:
        """
        Crée un noeud, l'étiquette est donnée en argument, les attributs sont :
        - val : l'etiquette
        - fg et fd : initialisés à None tout les deux
        """
        self.val = val
        self.fg = None
        self.fd = None


    def est_feuille(self) -> bool :
        """
        renvoie un booléen : True si self est une feuille, False sinon
        """
        return self.fg == None and self.fd == None

    def cree_fg(self, val) -> None:
        """
        val est une étiquette de type str
        Ajoute Node(val) en fils gauche
        """
        self.fg = Node(val)

    def cree_fd(self, val) -> None:
        """
        val est une étiquette de type str
        Ajoute Node(val) en fils droit
        """
        self.fd = Node(val)

    def __str__(self) -> str:
        """ renvoie etiquette (etiquette_fg , etiquette_fils_droit) """
        if self.fg is not None :gauche = str(self.fg.val)
        else : gauche = str(None)
        if self.fd is not None :droit = str(self.fd.val)
        else : droit = str(None)
        lignes =  str(self.val) + "  ( "+ gauche +" , "+ droit + ")"
        #if self.fg is not None : lignes+=str(self.fg)
        #if self.fd is not None : lignes+=str(self.fd)
        return lignes

# Notre arbre sera modélisé avec un dictionnaire.
class Arbre :
    def __init__(self,etiquette) -> None:
        """
        Intialiste un objet Arbre
        Attribut noeuds (dict):
            Initialisé avec une seule clé : noeuds[etiquette] = Node[etiquette]
            la prodondeur de cette feuille est 0
        Attribut etiquette_racine :
            Initialisée à etiquette_racine (jamais modifiée)
        Si etiquette est égale à None on crée un arbre vide
        """
        self.noeuds={}
        self.noeuds[etiquette] = Node(etiquette)
        self.etiquette_racine = etiquette

    def empty(self) -> bool:
        """ renvoie True si self est vide, False sinon """
        return list(self.noeuds.keys()) == [None]

    def addG(self,etiquette_parent, etiquette_fils) -> None :
        """
        :param etiquette_parent: est une etiquette d'un noeud de l'arbre
        :param etiquette_fils: est l'etiquette du fils gauche à ajouter
        addG :
            - ajoute un fils gauche au noeud parent : noeud_parent.fg = Node(etiquette_fils)
            - modifie l'attribut noeuds de l'arbre :
            noeuds[etiquette_fils] = Node(etiquette_fils)
        """
        if etiquette_parent not in self.noeuds :
            raise ValueError("Le noeud parent " + etiquette_parent + " n'existe pas")
        if self.noeuds[etiquette_parent].fg is not None :
            raise ValueError("vous ne pouvez pas ajouter un fils droit à " + etiquette_parent + " il y en a déjà un")
        if etiquette_fils in self.noeuds :
            raise ValueError("Vous ne pouvez pas ajouter un noeud" + etiquette_fils + " il y en a déjà un")

        noeud_parent = self.noeuds[etiquette_parent]
        noeud_parent.cree_fg(etiquette_fils)
        self.noeuds[etiquette_fils] = noeud_parent.fg

    def addD(self,etiquette_parent, etiquette_fils) -> None :
        """
        :param etiquette_parent: est une etiquette d'un noeud de l'arbre
        :param etiquette_fils: est l'etiquette du fils droit à ajouter
        addD :
            - ajoute un fils droit au noeud parent : noeud_parent.fd = Node(etiquette_fils)
            - modifie l'attribut noeuds de l'arbre :
              noeuds[etiquette_fils] = Node(etiquette_fils)
        """
        if etiquette_parent not in self.noeuds :
            raise ValueError("Le noeud parent " + etiquette_parent + " n'existe pas")
        if self.noeuds[etiquette_parent].fd is not None :
            raise ValueError("vous ne pouvez pas ajouter un fils droit à " + etiquette_parent + " il y en a déjà un:" + str(self.noeuds[etiquette_parent].fd.val))
        if etiquette_fils in self.noeuds :
            raise ValueError("Vous ne pouvez pas ajouter un noeud" + etiquette_fils + " il y en a déjà un")

        noeud_parent = self.noeuds[etiquette_parent]
        self.noeuds[etiquette_parent].cree_fd(etiquette_fils)
        self.noeuds[etiquette_fils] = self.noeuds[etiquette_parent].fd

    def filsG(self,etiquette) -> bool:
        """
        :param self arbre:
        :param etiquette: une etiquette d'un noeud
        renvoie True si ce noeud à un fils gauche, False si le fils gauche est None
        """
        if etiquette not in self.noeuds :
            raise ValueError("Le noeud  " + etiquette + " n'existe pas")
        return not self.noeuds[etiquette].fg == None

    def filsD(self,etiquette) -> bool:
        """
        :param self arbre:
        :param etiquette: une etiquette d'un noeud
        renvoie True si ce noeud à un fils droit, False si le fils droit est None
        """
        if etiquette not in self.noeuds :
            raise ValueError("Le noeud  " + etiquette + " n'existe pas")
        return not self.noeuds[etiquette].fd == None

    def __str__(self) :
        """
        renvoie une str contenant une ligne pour chaque noeud de l'arbre :
        etiquette_parent : etiquette_fg, etiquette_fd

        """
        lignes = ''
        for k in self.noeuds.keys() :
            gauche = self.noeuds[k].fg.val if self.noeuds[k].fg is not None else  '-'
            droite = self.noeuds[k].fd.val if self.noeuds[k].fd is not None else '-'
            lignes += str(k)+ " : "+str(gauche)+" / "+str(droite)+'\n'
        return lignes

    def make_nodes(self,g,cle,verts=None) :
        """ fonction privée """

        if self.noeuds[cle].fg != None :
            self.make_nodes(g,self.noeuds[cle].fg.val,verts)
            g.edge('node'+str(self.noeuds[cle].val),'node'+str(self.noeuds[cle].fg.val))
        else :
            g.node('node'+str(self.noeuds[cle].val)+'_g','', color="grey", fixedsize='True', height='0.1', width='0.1',style='filled')
            g.edge('node'+str(self.noeuds[cle].val),'node'+str(self.noeuds[cle].val)+'_g')

        if self.noeuds[cle].fd != None :
            self.make_nodes(g,self.noeuds[cle].fd.val,verts)
            g.edge('node'+str(self.noeuds[cle].val),'node'+str(self.noeuds[cle].fd.val))
        else :
            g.node('node'+str(self.noeuds[cle].val)+'_d','', color="grey", fixedsize='True',height='0.1', width='0.1',style='filled')
            g.edge('node'+str(self.noeuds[cle].val),'node'+str(self.noeuds[cle].val)+'_d')


        if (verts is not None ) and  (self.noeuds[cle].val in verts):
            g.node('node'+str(self.noeuds[cle].val), str(self.noeuds[cle].val), color="green",style='filled')
        else :
            g.node('node'+str(self.noeuds[cle].val), str(self.noeuds[cle].val), color="lightblue",style='filled')

    def est_feuille(self,etiquette) -> bool:
        """ Renvoie True si le noeud etiquette est une feuille """

        if etiquette not in self.noeuds :
            raise ValueError("Le noeud  " + etiquette + " n'existe pas")

        noeud = self.noeuds[etiquette]
        return noeud.fg == noeud.fg == None

    def racine(self) :
        """ renvoie l objet Node associé à la racine """

        return self.noeuds[self.etiquette_racine]

    def get_etiquetteG(self) :
        """ renvoie l etiquette du fils gauche de la racine (None si fg = None) """

        if self.filsG(self.etiquette_racine) :
            return self.noeuds[self.etiquette_racine].fg.val

    def get_nodeG(self,etiquette) :
        """
        Renvoie l objet Node du fils gauche du noeud etiquette
        (None si fg = None)

        """

        if etiquette not in self.noeuds :
            raise ValueError("Le noeud  " + etiquette + " n'existe pas")

        if self.filsG(etiquette) :
            return self.noeuds[etiquette].fg

    def get_etiquetteD(self) :
        """ renvoie l etiquette du fils droit de la racine (None si fd = None) """

        if self.filsD(self.etiquette_racine) : return self.noeuds[self.etiquette_racine].fd.val

    def get_nodeD(self, etiquette) :
        """
        Renvoie l objet Node du fils droit du noeud etiquette
        (None si fd = None)
        """

        if etiquette not in self.noeuds :
            raise ValueError("Le noeud  " + etiquette + " n'existe pas")
        if self.filsD(etiquette) :
            return self.noeuds[etiquette].fd


    def sad(self,etiquette = None):
        """
        Renvoie un Arbre SAD du noeud etiquette.
        Si etiquette n'est pas présent, renvoie le SAD de la racine
        """

        if etiquette == None : etiquette = self.etiquette_racine

        if etiquette not in self.noeuds :
            raise ValueError("Le noeud  " + etiquette + " n'existe pas")

        if self.noeuds[etiquette].fd is None : return Arbre(None)
        a =  Arbre(self.noeuds[etiquette].fd.val)
        noeud = a.racine().val
        self.add_fils_gauche(a,noeud)
        return a

    def sag(self, etiquette = None):
        """
        Renvoie un Arbre SAG du noeud etiquette.
        Si etiquette n'est pas présent, renvoie le SAG de la racine
        """

        if etiquette == None : etiquette = self.etiquette_racine

        if etiquette not in self.noeuds :
            raise ValueError("Le noeud  " + etiquette + " n'existe pas")

        if self.noeuds[etiquette].fg is None : return Arbre(None)
        a =  Arbre(self.noeuds[etiquette].fg.val)
        noeud = a.racine().val
        self.add_fils_gauche(a,noeud)
        return a

    def add_fils_droite(self,a,noeud) :
        """ fonction privée """

        noeud_fils = self.get_nodeD(noeud)
        if noeud_fils is  None :  return

        else :
            a.addD(noeud,noeud_fils.val)
            noeud = noeud_fils.val
            self.add_fils_gauche(a,noeud)

    def add_fils_gauche(self,a,noeud) :
        """ fonction privée """
        self.add_fils_droite(a,noeud)
        noeud_fils = self.get_nodeG(noeud)
        if noeud_fils is  None : return
        else :
            a.addG(noeud,noeud_fils.val)
            noeud = noeud_fils.val
            self.add_fils_gauche(a,noeud)

    def show(self,etiquette = None, verts = None):
        """
        :param etiquette: etiquette d'un noeud de l Arbre self
        :param verts: une liste d etiquettes dont les noeuds seront coloriés en vert
        Dessine l'arbre en partant du noeud etiquette
        si etiquette n'est pas présent, dessinne l'Arbre entier.
        """

        if self.empty():
            print("arbre vide")
            return

        if etiquette == None : etiquette = self.etiquette_racine
        if verts == None : verts = []

        if etiquette not in self.noeuds :
            print("il n'y a pas de noeud",etiquette,"dans l'arbre")
            return

        g = graphviz.Digraph('g', format='svg')

        self.make_nodes(g, etiquette, verts)
        return g

def addNodes(arbre) :
      """ ajout de tous les noeuds (fonction buggé il en manque)"""
      arbre.addG("04","14")
      arbre.addG("14","24")
      arbre.addG("24","23")
      arbre.addD("24","34")
      arbre.addG("23","22")
      arbre.addD("23","33")
      arbre.addD("22","32")
      arbre.addG("32","31")
      arbre.addG("31","21")
      arbre.addG("21","11")
      arbre.addD("21","20")
      arbre.addG("11","10")
      arbre.addG("10","00")
      arbre.addG("00","01")
      arbre.addG("20","30")
      arbre.addG("30","40")
      arbre.addD("31","41")
      arbre.addG("22","12")
      arbre.addG("12","13")
      arbre.addG("13","03")
      arbre.addG("34","44")
      arbre.addG("44","43")
      arbre.addG("43","42")
      arbre.addG("42","52")
      arbre.addD("52","53")
      arbre.addG("53","54")


def make_it() :
      """ construit l'arbre complet """
      arbre=Arbre("04")
      arbre.addG("04","14")
      arbre.addG("14","24")
      arbre.addG("24","23")
      arbre.addD("24","34")
      arbre.addG("23","22")
      arbre.addD("23","33")
      arbre.addD("22","32")
      arbre.addG("32","31")
      arbre.addG("31","21")
      arbre.addG("21","11")
      arbre.addD("21","20")
      arbre.addG("11","10")
      arbre.addG("10","00")
      arbre.addG("00","01")
      arbre.addG("20","30")
      arbre.addG("30","40")
      arbre.addD("31","41")
      arbre.addG("22","12")
      arbre.addG("12","13")
      arbre.addG("13","03")
      arbre.addG("34","44")
      arbre.addG("44","43")
      arbre.addG("43","42")
      arbre.addG("42","52")
      arbre.addD("52","53")
      arbre.addG("53","54")
      arbre.addG("03","02")
      arbre.addG("52","51")
      arbre.addG("51","50")
      return arbre

def test_arbre(arbre) :
    # teste si l'arbre est ok
    a = make_it()
    for cle in a.noeuds :
        assert cle in arbre.noeuds,"Votre arbre ne contient pas le noeud "+str(cle)
    print("test1 ok: votre arbre contient tous les noeuds")
    for cle in arbre.noeuds :
        assert cle in a.noeuds,"Votre arbre contient un noeud "+str(cle)+" surnuméraire"
    print("test2 ok: votre arbre ne contient pas de noeud surnuméraire")


    for cle in a.noeuds :
        #print(a.noeuds[cle],arbre.noeuds[cle])
        if a.noeuds[cle].fg == None :
            assert arbre.noeuds[cle].fg == None , "Le fils gauche du noeud "+str(cle)+" de votre arbre est "+str(arbre.noeuds[cle].fg.val)+" et devrait être None"
        else :
            assert a.noeuds[cle].fg.val == arbre.noeuds[cle].fg.val,"Le fils gauche du noeud "+str(cle)+" de votre arbre est "+str(arbre.noeuds[cle].fg.val)+" ce n'est pas correct"
        if a.noeuds[cle].fd == None :
            assert arbre.noeuds[cle].fd == None  , "Le fils droit du noeud "+str(cle)+" de votre arbre est "+str(arbre.noeuds[cle].fg.val)+" et devrait être None"
        else :
            assert a.noeuds[cle].fd.val == arbre.noeuds[cle].fd.val,"Le fils droit du noeud "+str(cle)+" de votre arbre est "+str(arbre.noeuds[cle].fd.val)+" ce n'est pas correct"
    print("test3 ok: votre arbre est correct")