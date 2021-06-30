def dica(secreto):
    dicas = ''
    lista = ['O número é impar','O número é divisível por 22','O número está num intervalo de 1 e 1432','A raiz desse número é maior que 32','O número é menor do que a idade do descobrimento do Brasil','O número é maior do que a quantidade de estados brasileiros']
    if secreto % 2 != 0 and dicas == '':
        if 'O número é impar' in lista:
            dicas = 'O número é impar'
            lista.pop(lista.index('O número é impar'))

    if secreto % 22 == 0 and dicas == '':
        if 'O número é divisível por 22' in lista:
            dicas = 'O número é divisível por 22'
            lista.pop(lista.index('O número é divisível por 22'))

    if secreto >= 1 and secreto < 1432 and dicas == '':
        if 'O número está num intervalo de 1 e 1432' in lista:
            dicas = "O número está num intervalo de 1 e 1432"
            lista.pop(lista.index('O número está num intervalo de 1 e 1432'))

    if secreto ** 1/2 > 32 and dicas == '':
        if 'A raiz desse número é maior que 32' in lista:
            dicas = 'A raiz desse número é maior que 32'
            lista.pop(lista.index('A raiz desse número é maior que 32'))

    elif secreto < 520 and dicas == '':
        if 'O número é menor do que a idade do descobrimento do Brasil' in lista:
            dicas = 'O número é menor do que a idade do descobrimento do Brasil'
            lista.pop(lista.index('O número é menor do que a idade do descobrimento do Brasil'))

    elif secreto > 24 and dicas == '':
        if 'O número é maior do que a quantidade de estados brasileiros' in lista:
            dicas = 'O número é maior do que a quantidade de estados brasileiros'
            lista.pop(lista.index('O número é maior do que a quantidade de estados brasileiros'))