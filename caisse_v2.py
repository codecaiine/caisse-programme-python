total_achats = 0
liste_prix = []
dix_mille = 0
cinq_mille = 0
deux_mille = 0
mille = 0
cinq_cent = 0
deux_cent = 0
cent = 0
cinqante = 0
vingt_cinq = 0

print("Bienvenue Boutique")

total_recettes = 0
for client in range(1,6):
    print("Entrez la facture du client numéro ", client, " . ")
    if client > 1 or client < 6:
        prix_article = 1
        while prix_article !=0:
            prix_article = int(input("Veuillez saisir le prix de l article : "))
            liste_prix.append(prix_article)
            total_achats = total_achats + prix_article
            print("Le total des achats est : ", total_achats, " FCFA")
