import heapq
# Configuration de l'état final
etat_final = "123456780"

# Définition des mouvements possibles : haut, bas, gauche, droite
# (décalage_ligne, décalage_colonne)
mouvements = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def est_deplacement_valide(pos,deplacement):
    ligne,colonne = divmod(pos,3)
    nouvelle_ligne,nouvelle_colonne= ligne + deplacement[0] , colonne + deplacement[1]
    return 0 <= nouvelle_ligne < 3 and 0 <= nouvelle_colonne < 3

def echanger (etat, pos1, pos2):
 ##Retourne un nouvel etat après avoir échangé les positions pos1 et pos2
    etat_liste = list (etat)
    etat_liste[pos1], etat_liste[pos2] = etat_liste[pos2], etat_liste[pos1]
    return  ''.join (etat_liste) ## converti en str

def dijkstra(etat_initial):
    """Implémente l'algorithme de Dijkstra pour résoudre le puzzle 8"""
    
    pq = [(0, etat_initial)]  
    visites = set()
    visites.add(etat_initial)
    etat_precedent = {etat_initial: None}

    while pq:
        cout_actuel, etat_actuel = heapq.heappop(pq)
        if etat_actuel == etat_final:
            chemin = []
            while etat_actuel is not None:
                chemin.append(etat_actuel)
                etat_actuel = etat_precedent[etat_actuel]
            return chemin[::-1] 
        position_trou = etat_actuel.index('0')
        for mouvement in mouvements:
            if est_deplacement_valide(position_trou, mouvement):
                nouvelle_ligne, nouvelle_colonne = divmod(position_trou, 3)
                nouvelle_ligne, nouvelle_colonne = nouvelle_ligne + mouvement[0], nouvelle_colonne + mouvement[1]
                nouvelle_position = nouvelle_ligne * 3 + nouvelle_colonne
                nouvel_etat = echanger(etat_actuel, position_trou, nouvelle_position)
                if nouvel_etat not in visites:
                    visites.add(nouvel_etat)
                    heapq.heappush(pq, (cout_actuel + 1, nouvel_etat))
                    etat_precedent[nouvel_etat] = etat_actuel

    return None  

etat_initial = "148762530"


chemin = dijkstra(etat_initial)

if chemin:
    print("Solution trouvée ! Voici les étapes :")
    for etape in chemin:
        print(etape)
else:
    print("Pas de solution trouvée.")

