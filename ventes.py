from database import connect_db
from datetime import datetime

def enregistrer_vente():
    produit_id = int(input("ID produit: "))
    quantite = int(input("Quantité: "))

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT prix, stock FROM produits WHERE id = ?", (produit_id,))
    produit = cursor.fetchone()

    if produit:
        prix, stock = produit

        if stock >= quantite:
            total = prix * quantite
            date = datetime.now().strftime("%Y-%m-%d")

            cursor.execute("INSERT INTO ventes (produit_id, quantite, total, date) VALUES (?, ?, ?, ?)",
                           (produit_id, quantite, total, date))

            cursor.execute("UPDATE produits SET stock = stock - ? WHERE id = ?",
                           (quantite, produit_id))

            conn.commit()
            print("Vente enregistrée !")
        else:
            print("Stock insuffisant !")
    else:
        print("Produit introuvable !")

    conn.close()
