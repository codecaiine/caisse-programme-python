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

while reste > 10000:
    dix_mille +=1
    reste-= 10000
while reste > 5000:
    cinq_mille +=1
    reste-= 5000
while reste > 2000:
    deux_mille +=1
    reste-= 2000
while reste > 1000:
    mille +=1
    reste-= 1000
while reste > 500:
    cinq_cent +=1
    reste-= 500
while reste > 200:
    deux_cent +=1
    reste-= 200
while reste > 100:
    cent +=1
    reste-= 100
while reste > 50:
    cinqante +=1
    reste-= 50

print('Il y a {} billet(s) de 10.000 FCFA'.format(dix_mille))
print('Il y a {} billet(s) de 5.000 FCFA'.format(cinq_mille))
