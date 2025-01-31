def est_deplacement_valide(pos,deplacement):
    ligne,colonne = divmod(pos,3)
    nouvelle_ligne,nouvelle_colonne= ligne + deplacement[0] , colonne + deplacement[1]
    return 0 <= nouvelle_ligne < 3 and 0 <= nouvelle_colonne < 3
