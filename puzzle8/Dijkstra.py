def est_deplacement_valide(pos,deplacement):
    ligne,colonne = divmod(pos,3)
    nouvelle_ligne,nouvelle_colonne= ligne + deplacement[0] , colonne + deplacement[1]
    return 0 <= nouvelle_ligne < 3 and 0 <= nouvelle_colonne < 3

def echanger (etat, pos1, pos2):
 ##Retourne un nouvel etat après avoir échangé les positions pos1 et pos2
    etat_ liste = list (etat)
    etat_ liste[pos1], etat_ liste[pos2] = etat_liste[pos2], etat_liste[pos1]
    return  ''.join (etat_liste) ## converti en str
