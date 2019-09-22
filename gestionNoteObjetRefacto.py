import random


class Classe:
    def __init__(self, id, nom):
        self.id = id
        self.nom = nom
        self.eleves = []
        self.matieres = []
        self.moyennesClasse = []

    def ajouterEleve(self, nom):
        nouvEleve = Eleve(len(self.eleves) + 1, nom)
        self.eleves.append(nouvEleve)
        for matiere in self.matieres:
            nouvEleve.bulletin.append(Bulletin(nouvEleve, matiere))


    def afficheEleves(self):
        for eleve in self.eleves:
            print(eleve)
            
    def ajouterMatiere(self, nomMatiere):
        nouvMatiere = Matiere(len(self.matieres) + 1, nomMatiere)
        self.matieres.append(nouvMatiere)
        
    def afficheMatieres(self):
        for matiere in self.matieres:
            print(matiere)
    
    


    
        
class Eleve:
    def __init__(self, id, nom):
        self.id = id
        self.nom = nom        
        self.moyenneGen = float
        self.bulletin = []
    

    def __str__(self):
     return "{}-{}".format(self.id, self.nom)


class Matiere :
    def __init__(self, id, nomMatiere):
        self.id = id
        self.nomMatiere = nomMatiere
        self.notes = []
        self.moyennes =[] 
        
    def ajouterNote(self, note):
        self.notes.append(note)

    def afficherNote(self):
        for note in self.notes:
            print(note)

    def chercherNotes(self, eleve, matiere):
        resultat = []

        for note in self.notes:
            if note.eleve.id == eleve.id and note.matiere.id == matiere.id:
                resultat.append(note)
        return resultat

    def __str__(self):
     return "{}-{}".format(self.id, self.nomMatiere)

class Bulletin :
    def __init__(self, eleve, matiere):
        self.eleve = eleve
        self.matiere = matiere
        self.notes = []
        self.moyenne = float


def main_menu():

    classe1 = Classe(1, 'CM1')

    stop = False
    while not stop :
        print ("Menu principal: \n 1. Ajouter une matière \n 2. Ajouter un élève \n 3. Saisir les notes d'un élève \n 4. Afficher les moyennes \n 5. Prix d'excellence \n 6. --- Remplir aleatoirement --- \n 7. Quitter le programme")

        selection = int((input("Entrez votre choix: ")))
        
                            
        if selection == 1:
            ajoutMatiere(classe1)

        elif selection == 2:                
            ajoutEleve(classe1)
        
        elif selection == 3:
            rentrerNote(classe1, Eleve, Matiere)
        
        elif selection == 4:
            calculer_moyenne(classe1, Matiere)
        
        elif selection == 5:
            calculer_excellence()

        elif selection == 6:
            remplirAleatoirement(classe1)
            
        elif selection == 7:
            stop = True
        else:
            print("Entrez un chiffre entre 1 et 6")





def ajoutMatiere(classe):
        
        if classe :
                classe.afficheMatieres()

        stop = False
        while not stop :                
                ajoutMatiere = input("\nTapez la matiere à ajouter puis validez avec entree ou tapez 'exit' pour revenir au menu principal\n")
                
                if ajoutMatiere != "exit":
                        classe.ajouterMatiere(ajoutMatiere)
                        classe.afficheMatieres()
                else :
                        stop = True 
    
def ajoutEleve(classe):
        
        if classe :
                classe.afficheEleves()
                
        stop = False
        while not stop :                
                ajoutEleve = input("\nTapez l'eleve à ajouter puis validez avec entree ou tapez 'exit' pour revenir au menu principal\n")
                
                if ajoutEleve != "exit":
                        classe.ajouterEleve(ajoutEleve)
                        classe.afficheEleves()
                else :
                        stop = True  

def rentrerNote(classe, eleve, matiere):

        if classe :
                classe.afficheEleves()
    
        stop = False
        while not stop :
        
            indexEleve = int(input("Tapez le numero de l'eleve à noter ou tapez 99 pour revenir au menu principal : "))
            if indexEleve != 99:
                elevesFiltre = list(filter(lambda e: e.id == indexEleve, classe.eleves))


                if (elevesFiltre and len(elevesFiltre) > 0) :
                    eleve = elevesFiltre[0]


                    for indexMatiere in range(0, len(classe.matieres)):
                        matiere = classe.matieres[indexMatiere]
                        print (("Matiere selectionnee : {}").format(matiere.nomMatiere))
                        
                        for trimestre in range (0,3):                            
                            note = int(input("Saisir la note : "))
                            matiere.ajouterNote(note)
            else :
                stop = True
            
        

def calculer_moyenne(classe, matiere):

        print("------- Moyenne par Eleve par matiere -------")

        for indexEleve in range(0, len(classe.eleves)):
            eleve = classe.eleves[indexEleve]
        
            for indexMatiere in range(0, len(classe.matieres)):
                matiere = classe.matieres[indexMatiere]
                
                somme = 0
                for note in matiere.notes :
                    somme = somme + note
                    
                matiere.moyennes = round(somme/10, 3)
                
                print(somme) 

       
        

        # print("---------- Moyenne de la classe par matiere -----------")

        # for indexMatiere in range (0, len(classeEleve.matieres)):
        #     matiere = classeEleve.matieres[indexMatiere]
        #     eleve = classeEleve.eleves[indexEleve]

   
        #     moyenneMatiere = classeEleve.chercherNotes(eleve, matiere)

        #     somme=0
        #     for note in moyenneMatiere :
        #         somme = somme + note.note

        #     classeEleve.moyennesClasse = somme

        #     print(classeEleve.moyennesClasse)







        # print("--------------- Moyenne generale par eleve -------")

        

        

        # print("----------- Moyenne generale classe -------------")
                
                
        # somme = 0
        # for note in classeEleve.notes :
        #     somme = somme + note.note

        # moyenneGenerale = round(somme /150, 2)      

                    
        # print(moyenneGenerale)
    
        

    
def calculer_excellence():
    print("prix d'excellence")

def ajoutEleveAlea(classe):        
        
    while not len(classe.eleves) >= 10 :
        ajout_eleve = "eleve_{}".format(len(classe.eleves))
        classe.ajouterEleve(ajout_eleve)
    classe.afficheEleves()

def ajoutMatiereAlea(classe):
        
    while not len(classe.matieres) >= 5 :
        ajout_matiere = "matiere_{}".format(len(classe.matieres))
        classe.ajouterMatiere(ajout_matiere)
    classe.afficheMatieres()

    
def ajoutNoteAlea(classe, matiere):
    
    for indexEleve in range(0, len(classe.eleves)):
        eleve = classe.eleves[indexEleve]
        
        for indexMatiere in range(0, len(classe.matieres)):
            matiere = classe.matieres[indexMatiere]   

            for trimestre in range(0, 3):
                note = round(random.uniform(0, 20))
                matiere.ajouterNote(note)                
                matiere.afficherNote()

    
def remplirAleatoirement(classe):
    ajoutEleveAlea(classe)
    ajoutMatiereAlea(classe)
    ajoutNoteAlea(classe, Matiere)


if __name__ == "__main__":
        main_menu()




