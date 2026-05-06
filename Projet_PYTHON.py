
# 1. Classe Etudiant
class Etudiant:
    def __init__(self, nom, prenom, sexe, date_naissance, lieu_naissance):
        # Attributs privés
        self.__nom = nom
        self.__prenom = prenom
        self.__sexe = sexe
        self.__date_naissance = date_naissance
        self.__lieu_naissance = lieu_naissance

    # Getters
    def get_nom(self): return self.__nom
    def get_prenom(self): return self.__prenom
    def get_sexe(self): return self.__sexe
    def get_date_naissance(self): return self.__date_naissance
    def get_lieu_naissance(self): return self.__lieu_naissance

    # Setters
    def set_nom(self, nom): self.__nom = nom
    def set_prenom(self, prenom): self.__prenom = prenom
    def set_sexe(self, sexe): self.__sexe = sexe
    def set_date_naissance(self, date): self.__date_naissance = date
    def set_lieu_naissance(self, lieu): self.__lieu_naissance = lieu

    # 2. Méthode Infos_Etudiant()
    def Infos_Etudiant(self):
        print("\n--- Infos Étudiant ---")
        print("Nom :", self.__nom)
        print("Prénom :", self.__prenom)
        print("Sexe :", self.__sexe)
        print("Date de naissance :", self.__date_naissance)
        print("Lieu de naissance :", self.__lieu_naissance)

    # ➤ Méthode simple pour enregistrer dans un fichier CSV
    def enregistrer_base(self):
        with open("etudiants.csv", "a") as f:
            f.write(f"{self.__nom},{self.__prenom},{self.__sexe},{self.__date_naissance},{self.__lieu_naissance}\n")
        print("Infos enregistrées dans la base.")

# 3. Fonction Inscription (hors de la classe)
def Inscription():
    print("=== INSCRIPTION ===")
    nom = input("Nom : ")
    prenom = input("Prénom : ")
    sexe = input("Sexe (M/F) : ")
    date_naissance = input("Date de naissance (JJ/MM/AAAA) : ")
    lieu_naissance = input("Lieu de naissance : ")

    # Création de l'objet étudiant
    E = Etudiant(nom, prenom, sexe, date_naissance, lieu_naissance)
    E.Infos_Etudiant()

    enregistrer = input("Enregistrer ? (o/n) : ")
    if enregistrer.lower() == "o":
        E.enregistrer_base()
        E.FICHE_INSCRIPTION()

# 4. Méthode FICHE_INSCRIPTION() dans la classe Etudiant
    # On la place ici car elle est utilisée dans Inscription
def FICHE_INSCRIPTION(self):
    nb_matieres = int(input("Combien de matières ? "))
    total = 0
    reussies = 0
    matieres_a_améliorer = []
    notes = {}

    for i in range(nb_matieres):
        matiere = input(f"Matière {i+1} : ")
        note = float(input("Note sur 20 : "))
        notes[matiere] = note
        total += note
        if note >= 12:
            reussies += 1
        else:
            matieres_a_améliorer.append(matiere)

    print("\n--- Bulletin ---")
    self.Infos_Etudiant()
    for matiere, note in notes.items():
        print(f"{matiere} : {note}/20")

    moyenne = total / nb_matieres
    pourcentage = (reussies / nb_matieres) * 100

    print(f"Moyenne : {moyenne:.2f}/20")

    if pourcentage >= 80:
        print("Décision : Passe au niveau supérieur")
    else:
        print("Décision : Ne passe pas")

    if matieres_a_améliorer:
        print("Matières à améliorer :")
        for mat in matieres_a_améliorer:
            print("-", mat)

# Ajouter la méthode dans la classe
Etudiant.FICHE_INSCRIPTION = FICHE_INSCRIPTION

# Lancer le programme
Inscription()

