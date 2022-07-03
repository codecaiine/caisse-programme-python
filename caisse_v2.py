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
for client in range(1,3):
    print("Entrez la facture du client numéro ", client, " . ")
    if client > 1 or client < 3:
        prix_article = 1
        while prix_article !=0:
            prix_article = int(input("Veuillez saisir le prix de l article : "))
            total_achats += prix_article
            print("Le total des achats est : ", total_achats, " FCFA")

            montant_client = int(input('Saisissez le montant rémis par le client : '))
            print("Le client a rémis")
            monnaie = montant_client - total_achats
            print("Il vous reste ", monnaie, " FCFA comme monnaie restant .")

        total_recettes += total_achats
print("Total recette", total_recettes)
