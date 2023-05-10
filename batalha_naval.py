import random

def define_posicoes(linha, coluna, orientacao, tamanho):
    nova_lista = []

    if orientacao == 1:
        for i in range(tamanho):
            nova_lista.append([linha + i, coluna])

    elif orientacao == 2:
        for i in range(tamanho):
            nova_lista.append([linha, coluna + i])

    return nova_lista


def preenche_frota(frota, nome, linha, coluna, orientacao, tamanho):
        
    posicao = define_posicoes(linha, coluna, orientacao, tamanho)

    if nome not in frota:
        frota[nome] = list()
    
    frota[nome].extend([posicao])

    return frota

def faz_jogada(tabuleiro, linha, coluna):

    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    
    else: tabuleiro[linha][coluna] = '-'

    return tabuleiro

def posiciona_frota(frota):

    grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    for key in frota:
        for coordenadas_lista in frota[key]:
            for coordenadas in coordenadas_lista:
                i, j = coordenadas
                grid[i][j] = 1

    return grid

def afundados(frota, tabuleiro):
    
    counter = 0
    afundado = 0

    for locate in frota:
        for coordenadas_lista in frota[locate]:
            counter = 0
            for coordenadas in coordenadas_lista:

                i, j = coordenadas

                if tabuleiro[i][j] == 'X':
                    counter += 1

                if len(coordenadas_lista) == counter:
                    afundado += 1
    
    return afundado

def posicao_valida(frota, linha, coluna, orientacao, tamanho): 

    validar = define_posicoes(linha, coluna, orientacao, tamanho)

    for arrays in validar:
        for verifica_apos_alocacao in arrays:
            if verifica_apos_alocacao > 9:
                return False
        
    
    for navio in frota:
        for coordenadas_lista in frota[navio]:
            for coordenadas in coordenadas_lista:
               for valores in validar:

                    if coordenadas == valores:
                        return False
                    
    return True

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto         

    

frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

ctrlescolha = 0

for nomes_navios in frota.keys():
    ctrlescolha += 1
    for j in range(ctrlescolha):

        tamanho = 5 - ctrlescolha

        validacao_posicao_valida = False

        while validacao_posicao_valida != True:
            print("Insira as informacoes referentes ao navio " + nomes_navios + " que possui tamanho " + str(tamanho))

            linha = int(input("Linha : "))
            coluna = int(input("Coluna : "))

            if tamanho != 1:
                orientacao = int(input("[1] Vertical [2] Horizontal >"))

            validacao_posicao_valida = posicao_valida(frota, linha, coluna, orientacao, tamanho)

            if validacao_posicao_valida != True:
                print("Esta posição não está válida!")
            
            else:                
                frota = preenche_frota(frota, nomes_navios, linha, coluna, orientacao, tamanho)


tabuleiro_jogador = posiciona_frota(frota)
tabuleiro_oponente = posiciona_frota(frota_oponente)

jogando = True

lista_jogadas = []
lista_jogadas_oponente = []
jogada_oponente_valida = True

ctrl_lista_jogadas = 0
valido = True
check_valido = False
check_valido_oponente = False


while(jogando):

    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
    valido = True

    while(valido):

        check_valido = False

        linha_jogada = int(input("Jogador, qual linha deseja atacar? "))

        while(linha_jogada < 0 or linha_jogada > 9):
            linha_jogada = int(input("Jogador, qual linha deseja atacar? "))

            if(linha_jogada < 0 or linha_jogada > 9):
                print("Linha inválida!")

        coluna_jogada = int(input("Jogador, qual coluna deseja atacar? "))

        while(coluna_jogada < 0 or coluna_jogada > 9):
            coluna_jogada = int(input("Jogador, qual coluna deseja atacar? "))

            if(coluna_jogada < 0 or coluna_jogada > 9):
                print("Coluna inválida!")

        i = 0

        while i < len(lista_jogadas):

            if lista_jogadas[i] == linha_jogada and lista_jogadas[i + 1] == coluna_jogada:
                print("A posição linha " + str(linha_jogada) + " e coluna " + str(coluna_jogada) + " já foi informada anteriormente!")

                del lista_jogadas[i]
                del lista_jogadas[i]
                check_valido = True

            else: i += 2
             

        lista_jogadas.append(linha_jogada)
        lista_jogadas.append(coluna_jogada)

        if check_valido == False:
            valido = False

    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha_jogada, coluna_jogada)

    ctrl_lista_jogadas += ctrl_lista_jogadas + 2

    check_afundados = afundados(frota_oponente, tabuleiro_oponente)

    if check_afundados == 10:
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando = False

    else:

        jogada_oponente_valida = True

        while(jogada_oponente_valida):

            check_valido_oponente = False

            ataque_linha_oponente = random.randint(0, 9)
            ataque_coluna_oponente = random.randint(0, 9)

            j = 0

            while j < len(lista_jogadas_oponente):

                if lista_jogadas_oponente[j] == ataque_linha_oponente and lista_jogadas_oponente[j + 1] == ataque_coluna_oponente:

                    del lista_jogadas_oponente[j]
                    del lista_jogadas_oponente[j]

                    check_valido_oponente = True

                else: j += 2

            lista_jogadas_oponente.append(ataque_linha_oponente)
            lista_jogadas_oponente.append(ataque_coluna_oponente)

            if check_valido_oponente == False:
                jogada_oponente_valida = False
            
        print("Seu oponente está atacando na linha " + str(ataque_linha_oponente) + " e coluna " + str(ataque_coluna_oponente))

        faz_jogada(tabuleiro_jogador, ataque_linha_oponente, ataque_coluna_oponente)
        jogada_oponente_valida = False
        
        check_afundados_oponente = afundados(frota, tabuleiro_jogador)

        if check_afundados_oponente == 10:
            print("Xi! O oponente derrubou toda a sua frota =(")
            jogando = False






    











