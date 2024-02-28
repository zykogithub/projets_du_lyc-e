################################## ANNEXE ###################################
#                    contenu du module visu_tree                            #
#       A mettre dans un module importé dans la session                     #
#############################################################################

class Arbre :
    def __init__(self, val=None) :
        self.val = val
        self.fils_g = None
        self.fils_d = None

    def ajout_g(self,val) :
        self.fils_g = Arbre(val) # on ajoute un Noeud
    def ajout_d(self,val) :
        self.fils_d = Arbre(val) # on ajoute un Noeud

    def __str__(self):
        if self.fils_g is not None :gauche = str(self.fils_g.val)
        else : gauche = str(None)
        if self.fils_d is not None :droit = str(self.fils_d.val)
        else : droit = str(None)
        lignes =  str(self.val) + "  ( "+ gauche +" , "+ droit + ")\n"
        if self.fils_g is not None : lignes+=str(self.fils_g)
        if self.fils_d is not None : lignes+=str(self.fils_d)
        return lignes

    def make_nodes(self,g) :

        if self.fils_g != None :
            self.fils_g.make_nodes(g)
            g.edge('node'+str(self.val),'node'+str(self.fils_g.val))
        else :
            g.attr('node', shape='circle', fixedsize='true', width='0.1',fillcolor='lightgrey',style='filled')
            g.node('node'+str(self.val)+'_g','')
            g.attr('node', shape='ellipse', fixedsize='true', width='1',fillcolor='white',style='')
            g.edge('node'+str(self.val),'node'+str(self.val)+'_g')

        if self.fils_d != None :
            self.fils_d.make_nodes(g)
            g.edge('node'+str(self.val),'node'+str(self.fils_d.val))
        else :
            g.attr('node', shape='circle', fixedsize='true', width='0.1',fillcolor='lightgrey',style='filled')
            g.node('node'+str(self.val)+'_d','')
            g.edge('node'+str(self.val),'node'+str(self.val)+'_d')

        g.attr('node', shape='ellipse', fixedsize='true', width='1',fillcolor='white',style='')
        g.node('node'+str(self.val), str(self.val))



    def show(self):
        import graphviz
        from graphviz import nohtml
        g = graphviz.Digraph('g', format='svg')
        self.make_nodes(g)
        return g



