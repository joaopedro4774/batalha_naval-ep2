def afundados(frota, tabuleiro):
    
    counter = 0
    afundado = 0

    for key in frota:
        for coordenadas_lista in frota[key]:
            counter = 0
            for coordenadas in coordenadas_lista:

                i, j = coordenadas

                if tabuleiro[i][j] == 'X':
                    counter += 1

                if len(coordenadas_lista) == counter:
                    afundado += 1
    
    return afundado