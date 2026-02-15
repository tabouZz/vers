from database import create_tables
import employes
import produits
import ventes
import depenses

create_tables()

while True:
    print("\n===== GESTION ENTREPRISE =====")
    print("1. Ajouter employé")
    print("2. Voir employés")
    print("3. Ajouter produit")
    print("4. Voir produits")
    print("5. Enregistrer vente")
    print("6. Ajouter dépense")
    print("7. Quitter")

    choix = input("Choix: ")

    if choix == "1":
        employes.ajouter_employe()
    elif choix == "2":
        employes.afficher_employes()
    elif choix == "3":
        produits.ajouter_produit()
    elif choix == "4":
        produits.afficher_produits()
    elif choix == "5":
        ventes.enregistrer_vente()
    elif choix == "6":
        depenses.ajouter_depense()
    elif choix == "7":
        print("Au revoir !")
        break
    else:
        print("Choix invalide !")
