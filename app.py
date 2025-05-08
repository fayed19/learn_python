###Les conceptes
# ✅ La création de classes et d’objets
# ✅ L'encapsulation (_attribut et __attribut)
# ✅ L'héritage (class Fille(Mère))
# ✅ Le polymorphisme (surcharge de méthodes)
# ✅ L'abstraction : Forcer la réécriture d'une methode d'une classe
# ✅ La Composition: construire une classe en utilisant d'autres classes comme composants.


from abc import ABC, abstractmethod

class Forme(ABC):
    @abstractmethod
    def calculer_surface():
        pass

class Rectangle(Forme):
    def __init__(self, Longeur, largeur):
        self.L = Longeur
        self.l = largeur

    def calculer_surface(self):
        surface = self.L * self.l 
        print(f"La surface du rectangle est {surface}")

class Cercle(Forme):
    t = 3.14
    def __init__(self, rayon):
        self.r = rayon

    def calculer_surface(self):
        surface = self.r * self.r * Cercle.t
        print(f"La surface du cercle est {surface}")



# cercle_01 = Cercle(5)
# rectangle_01 = Rectangle(10, 7)

# liste_formes = [cercle_01, rectangle_01]

# for forme in liste_formes:
#     forme.calculer_surface()

class Voiture:
    voiture_crees = 0

    def __init__(self, marque, couleur):
        Voiture.voiture_crees+=1
        self.marque = marque
        self.couleur = couleur

    def demarrer(self):
        print(f"La voiture {self.marque} demarre ... ")


class CompteBancaire:
    def __init__(self, nom, solde):
        self.nom = nom
        self._solde = solde # attribut privé
    
    def deposer(self, montant):
        self._solde += montant

    def retirer(self, montant):
        if montant <= self._solde:
            self._solde -= montant
        else : 
            print("Fonds insuffisants.")

    def afficher_solde(self):
        print(f" Le solde de {self.nom} est de {self._solde}F")

    def afficher_infos(self):
        print(f"Compte de {self.nom} avec un solde de {self._solde}F.")


class CompteEpargne(CompteBancaire):

    def __init__(self, nom, solde, taux_interet):
        super().__init__(nom, solde)
        self.taux_interet = taux_interet

    def ajouter_interet(self):
        interet = self._solde * self.taux_interet / 100
        self._solde += interet
        print(f"Interêt de {interet}F ajouté. ")

    def afficher_infos(self):
        print(f"Compte Epargne de  {self.nom} - Solde : {self._solde}F - Taux : {self.taux_interet}%")



class Processeur:
    def afficher_info(self):
        print(f"Je suis le processeur")

class Ordinateur:
    processeur = Processeur()
    def afficher_info_processeur(self):
        Ordinateur.processeur.afficher_info()
        



ordi_01 = Ordinateur()

ordi_01.afficher_info_processeur()






#Utilisation 

# compte_01 = CompteBancaire("Traoré Paul", 3575)
# compte_02 = CompteEpargne("AYENA Djodjouwin Eudes Fourier", 3575, 5)

# liste_comptes = [compte_01, compte_02]

# for compte in liste_comptes:
#     compte.afficher_infos()

# print(Voiture.__dict__)
# print(CompteBancaire.__dict__)
# print(CompteEpargne.__dict__)
