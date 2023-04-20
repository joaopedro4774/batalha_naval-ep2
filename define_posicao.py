def define_posicoes(linha, coluna, orientacao, tamanho):
    nova_lista = []
    if orientacao == 'vertical':
        for i in range(tamanho):
            nova_lista.append([linha + i, coluna])
    elif orientacao == 'horizontal':
        for i in range(tamanho):
            nova_lista.append([linha, coluna + i])
    return nova_lista