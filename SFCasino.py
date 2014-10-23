import math
import random

class roulette:
    
    def demanderNumero(self):
        _numero = int(input("Sur quel numéro miser? "))
        if(not _numero in range(0,50)): raise ValueError
        return(_numero)

    def demanderMise(self,_pognon):
        _mise = int(input("Entrez votre mise:"))
        if(_mise > _pognon): raise ValueError
        return(_mise)

    def lancerLaRoulette(self,_numero,_mise,_pognon):
        resultat = random.randrange(0,50)
        if(_numero % 2 == 1):
            couleurChoisie = "noire"
        else:
            couleurChoisie = "rouge"
        if(resultat %2 == 1):
            couleurTiree = "noire"
        else:
            couleurTiree = "rouge" 
        print("\nresultat:{}\n".format(resultat))
        if(resultat == _numero):
            _pognon += _mise*3
            print("jackpot!!!!!\n")
        elif(couleurChoisie == couleurTiree):
            _pognon += math.ceil(_mise * 0.5)
            print("vous avez choisi la case {0} de couleur {1}, or, la boule est tombée sur une case {1} donc gagné!!!\n".format(_numero,couleurChoisie))
        else:
            _pognon -= _mise
            print("vous avez choisi la case {0} de couleur {1}, or, la boule est tombée sur une case {2} donc perdu!!!\n".format(_numero,couleurChoisie,couleurTiree))
        return _pognon

    def Main(self):           
        pognon = 1000
        while(pognon!=0):
            print("\nVous disposez actuellement de {}€".format(pognon))  
            try:
                numero = self.demanderNumero()
                mise = self.demanderMise(pognon)
            except:
                print("Erreur dans la saisie, veuillez réessayer...\n")
                continue
            pognon = self.lancerLaRoulette(numero,mise,pognon)



print("\nBienvenue au SFCasino™!!!\n")
print("Liste des activités:\n\t1.Roulette\n")
while(1):
    a = int(input("Entrez le numéro de l'activité:"))
    if(a==1):
        Roulette = roulette()
        Roulette.Main()
        break
    else:
        print("index inconnu, réessayer...\n")
