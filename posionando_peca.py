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


#pergunta navio-tanque

i = 0
while i < 3:

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


#pergunta contratorpedeiro

j = 0
while j < 4:

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

    
k = 0

#pergunta submarino

while k < 5:

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

    

print(frota)