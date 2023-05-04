def define_posicoes(linha, coluna, orientacao, tamanho):
    nova_lista = []
    if orientacao == 'vertical':
        for i in range(tamanho):
            nova_lista.append([linha + i, coluna])
    elif orientacao == 'horizontal':
        for i in range(tamanho):
            nova_lista.append([linha, coluna + i])
    return nova_lista

def preenche_frota(frota, nome, linha, coluna, orientacao, tamanho):
        
    posicao = define_posicoes(linha, coluna, orientacao, tamanho)

    if nome not in frota:
        frota[nome] = list()
    
    frota[nome].extend([posicao])

    return frota

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    novas_posicoes = define_posicoes(linha, coluna, orientacao, tamanho)

    posicoes_ocupadas = {}
    for nome_navio in frota:
        navios = frota[nome_navio]
        for i in range(len(navios)):
            navio = navios[i]
            for j in range(len(navio)):
                posicao = navio[j]
                posicoes_ocupadas[(posicao[0], posicao[1])] = True


    for i in range(len(novas_posicoes)):
        posicao = novas_posicoes[i]
        if posicao[0] < 0 or posicao[0] >= 10 or posicao[1] < 0 or posicao[1] >= 10:
            return False
        if (posicao[0], posicao[1]) in posicoes_ocupadas:
            return False
    return True

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

frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}
#perguntas porta avião


print('Insira as informações referentes ao navio porta-aviões que possui tamanho 4')
tamanho = 4
nome = 'porta-aviões'
while True:
    linha = int(input('Linha: '))
    coluna = int(input('Coluna: '))
    orientacao = int(input('[1] Vertical [2] Horizontal >'))
    if orientacao == 1:
        orientacao = 'vertical'
    else:
        orientacao = 'horizontal'
    if posicao_valida(frota, linha, coluna, orientacao, tamanho) == True:
        preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
        
        break

    else:
        print('Esta posição não está válida!')
        print('Insira as informações referentes ao navio porta-aviões que possui tamanho 4')


#pergunta navio-tanque

i = 0
while i < 2:

    print('Insira as informações referentes ao navio navio-tanque que possui tamanho 3')
    tamanho = 3
    nome = 'navio-tanque'
    while True:
        linha = int(input('Linha: '))
        coluna = int(input('Coluna: '))
        orientacao = int(input('[1] Vertical [2] Horizontal >'))
        if orientacao == 1:
            orientacao = 'vertical'
        else:
            orientacao = 'horizontal'
        if posicao_valida(frota, linha, coluna, orientacao, tamanho) == True:
            preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
            
            i+=1
            break

        else:
            print('Esta posição não está válida!')
            print('Insira as informações referentes ao navio navio-tanque que possui tamanho 3')


#pergunta contratorpedeiro

j = 0
while j < 3:

    print('Insira as informações referentes ao navio contratorpedeiro que possui tamanho 2')
    tamanho = 2
    nome = 'contratorpedeiro'
    while True:
        linha = int(input('Linha: '))
        coluna = int(input('Coluna: '))
        orientacao = int(input('[1] Vertical [2] Horizontal >'))
        if orientacao == 1:
            orientacao = 'vertical'
        else:
            orientacao = 'horizontal'
        if posicao_valida(frota, linha, coluna, orientacao, tamanho) == True:
            preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
            
            j+=1

            break

        else:
            print('Esta posição não está válida!')
            print('Insira as informações referentes ao navio contratorpedeiro que possui tamanho 2')

    
k = 0

#pergunta submarino

while k < 4:

    print('Insira as informações referentes ao navio submarino que possui tamanho 1')
    tamanho = 1
    nome = 'submarino'
    while True:
        linha = int(input('Linha: '))
        coluna = int(input('Coluna: '))
        if posicao_valida(frota, linha, coluna, orientacao, tamanho) == True:
            preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
            
            k+=1

            break

        else:
            print('Esta posição não está válida!')
            print('Insira as informações referentes ao navio submarino que possui tamanho 1')


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


def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto


tabuleiro_jogador = posiciona_frota(frota)
tabuleiro_oponente = posiciona_frota({})

jogando = True
while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
    while True:
        while True:
            linha = int(input('Jogador, qual linha deseja atacar? '))
            if linha < 0 or linha > 9:
                print('Linha inválida!')
            else:
                break
        
        while True:
            coluna = int(input('Jogador, qual coluna deseja atacar? '))
            if coluna < 0 or coluna > 9:
                print('Coluna inválida!')
            else:
                break
        
        if tabuleiro_oponente[linha][coluna] == 'X':
            print('A posição linha LINHA e coluna COLUNA já foi informada anteriormente!')
        else:
            tabuleiro_oponente[linha][coluna] = 'X'
            break
    
    if afundados(frota_oponente, tabuleiro_oponente) == 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando=False

    

