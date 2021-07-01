import random
def jogador(num_jogadores):
    jogadores = []
    for i in range(num_jogadores):
        nome = input('Nome do jogador %i' % (i+1))
        jogadores.append(nome)
    return jogadores

def rodadas(jogadores,secreto,dicas):
    palpites = []
    for x in range(5):
        dica = random.choice(dicas)
        dicas.pop(dicas.index(dica))
        if x >= 1:
            print(dica)
        for jogador in jogadores:
            print(jogador)
            palpite = int(input('Qual o seu palpite: '))
            x = [jogador, palpite]
            palpites.append(x)
        for palpite in palpites:
            if palpite[1] == secreto:
                break

def dica(secreto):
    dicas = []

    if secreto % 2 != 0:
        if 'O número é impar' not in dicas:
            dicas.append('O número é impar')
    else:
        if 'O número é par' not in dicas:
            dicas.append('O número é par')


    if secreto % 22 == 0:
        if 'O número é divisível por 22' not in dicas:
            dicas.append('O número é divisível por 22')


    if secreto >= 1 and secreto < 1432:
        if 'O número está num intervalo de 1 e 1432' not in dicas:
            dicas.append("O número está num intervalo de 1 e 1432")


    if secreto ** 1/2 > 32:
        if 'A raiz desse número é maior que 32' not in dicas:
            dicas.append('A raiz desse número é maior que 32')
    else:
        if 'A raiz desse número é menor que 32' not in dicas:
            dicas.append('A raiz desse número é menor que 32')


    if secreto < 520:
        if 'O número é menor do que a idade do descobrimento do Brasil' not in dicas:
            dicas.append('O número é menor do que a idade do descobrimento do Brasil')
    else:
        if 'O número é maior do que a idade do descobrimento do Brasil' not in dicas:
            dicas.append('O número é maior do que a idade do descobrimento do Brasil')


    if secreto > 24 :
        if 'O número é maior do que a quantidade de estados brasileiros' not in dicas:
            dicas.append('O número é maior do que a quantidade de estados brasileiros')
    else:
        if 'O número é menor do que a quantidade de estados brasileiros' not in dicas:
            dicas.append('O número é menor do que a quantidade de estados brasileiros')

    return dicas
