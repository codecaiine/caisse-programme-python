total = 0
listeValeur = []
dix_mille = 0
cinq_mille = 0
deux_mille = 0
mille = 0
cinq_cent = 0
deux_cent = 0
cent = 0
cinqante = 0

valeur = 1
while valeur !=0:
    try:
        valeur = int(input("Veuillez saisir le prix de l article : "))
        listeValeur.append(valeur)
        total = total + valeur
        print("Le total des achats est : ", total, " FCFA")
    except ValueError:
       print("Erreur! Veuillez entrer un prix correcte !")

montant_remis = int(input('Saisissez le montant rémis par le client : '))
print("Le client a rémis")
reste = montant_remis - total
print("Il vous reste ", reste, " FCFA comme monnaie restant .")