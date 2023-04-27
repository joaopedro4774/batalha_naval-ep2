def define_posicoes(linha, coluna, orientacao, tamanho):
    nova_lista = []
    if orientacao == 'vertical':
        for i in range(tamanho):
            nova_lista.append([linha + i, coluna])
    elif orientacao == 'horizontal':
        for i in range(tamanho):
            nova_lista.append([linha, coluna + i])
    return nova_lista


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