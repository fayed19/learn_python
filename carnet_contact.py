"""
Fonctionnalités prévues :
Ajouter un contact (nom, téléphone, email)

Afficher tous les contacts

Rechercher un contact par nom

Supprimer un contact

"""
import os


print("Carnet de contact : ")

class Contact:
    def __init__(self, nom, telephone, email):
        self.nom = nom
        self.telephone = telephone
        self.email = email
    
    def afficher_contact(self):
        print(f" {self.nom} | {self.telephone} | {self.email}")
    
    
    def supprimer_contact(self):
        pass


class CarnetContacts:
    def __init__(self, nom_fichier="contacts.txt"):
        self.contacts = []
        self.nom_fichier = nom_fichier
        self.charger_contacts()


    def afficher_tous_les_contacts(self):
        if not self.contacts:
            print("Aucun contact enrégistré.")
        else :
            for contact in self.contacts:
                print("----------------------------")
                contact.afficher_contact()

    def ajouter_contact(self, contact):
        self.contacts.append(contact)
        print(f"\nContact ajouté avec succès.")
        self.sauvegarder_contacts()

    def rechercher_contact(self, nom):
        trouve = False
        for contact in self.contacts:
            if contact.nom.lower() == nom.lower():
                contact.afficher_info()
                trouve = True
        if not trouve:
            print("Contact non retrouvé.")

    def sauvegarder_contacts(self):
        with open(self.nom_fichier, "w") as fichier:
            for contact in self.contacts:
                fichier.write(f"{contact.nom},{contact.telephone},{contact.email}\n")

        def supprimer_contact(self, nom):
            for contact in self.contacts:
                if contact.nom.lower() == nom.lower():
                    self.contacts.remove(contact)
                    print("Contact supprimé avec succès.")
                    self.sauvegarder_contacts()
                    return
            print("Contact non trouvé.")

        def modifier_contact(self, nom):
            for contact in self.contacts:
                if contact.nom.lower() == nom.lower():
                    nouveau_nom = input("Nouveau nom (laisser vide pour ne pas changer) : ")
                    nouveau_tel = input("Nouveau téléphone (laisser vide pour ne pas changer) : ")
                    nouvel_email = input("Nouvel email (laisser vide pour ne pas changer) : ")

                    if nouveau_nom:
                        contact.nom = nouveau_nom
                    if nouveau_tel:
                        contact.telephone = nouveau_tel
                    if nouvel_email:
                        contact.email = nouvel_email

                    print("Contact modifié avec succès.")
                    self.sauvegarder_contacts()
                    return
            print("Contact non trouvé.")



    def charger_contacts(self):
        if os.path.exists(self.nom_fichier):
            with open(self.nom_fichier, "r") as fichier:
                for ligne in fichier:
                    nom, telephone, email = ligne.strip().split(",")
                    contact = Contact(nom, telephone, email)
                    self.contacts.append(contact)

def afficher_menu():
    print("\n=== Carnet de Contacts ===")
    print("1. Ajouter un contact")
    print("2. Afficher tous les contacts")
    print("3. Rechercher un contact")
    print("4. Supprimer un contact")
    print("5. Modifier un contact")
    print("6. Quitter")

#Création du carnet
carnet = CarnetContacts()

while True:
    afficher_menu()
    choix = input("\n Choississez une option : ") 

    if choix == "1":
        nom = input("Nom : ")
        telephone = input("Téléphone : ")
        email = input("Email : ")
        nouveau_contact = Contact(nom, telephone, email)
        carnet.ajouter_contact(nouveau_contact)

    elif choix == "2":
        carnet.afficher_tous_les_contacts()

    elif choix == "3":
        nom = input("Entrez le nom à rechercher : ")
        carnet.rechercher_contact(nom)

    elif choix == "4":
        nom = input("Entrez le nom du contact à supprimer : ")
        carnet.supprimer_contact(nom)
    
    elif choix == "5":
        nom = input("Entrez le nom du contact à modifier : ")
        carnet.modifier_contact(nom)


    elif choix == "6":
        print("À bientôt !")
        break

    else:
        print("Option invalide. Veuillez réessayer.")




# contact_01 = Contact("AYENA Eudes", 61017482, "ayena2fourier@gmail.com")
# contact_02 = Contact("Alice", "12345", "alice@example.com")
# contact_03 = Contact("Bob", "67890", "bob@example.com")

# # contact_01.afficher_contact()


# carnet.ajouter_contact(contact_01)
# carnet.ajouter_contact(contact_02)
# carnet.ajouter_contact(contact_03)

# carnet.afficher_tous_les_contacts()
# carnet.rechercher_contact("Bob")
    
