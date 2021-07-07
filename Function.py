import random
def jogador(num_jogadores): ### para receber e cadastrar jogadores
    jogadores = []
    arq = open('cadastro.txt', 'r')#Leitura de arquivo
    nomes = []
    senhas = []
    for linha in arq.readlines():
        a = linha.split('|')
        lista = a
        nomes.append(lista[0])
        senhas.append(lista[1])
    arq.close()#Fechar arquivos
    while len(jogadores) < num_jogadores:
        nome = input('Nome do jogador: ').upper()
        if nome not in nomes:
            senha = input('Senha: ').upper()
            conf_senha = input('Confirme a senha: ').upper()
            if senha == conf_senha:
                print('Deseja confirmar o cadastro:\n1 - SIM\n2 - NÂO')
                opc = int(input())
                if opc == 1:
                    arquivo1 = open('cadastro.txt', 'a') #append em arquivos
                    arquivo1.write(nome + '|')
                    arquivo1.write(senha + '\n')
                    lista = [nome,senha]
                    jogadores.append(lista)
                    arquivo1.close() #Fechar arquivos
                else:
                    continue
            else:
                print('Senhas Diferentes')
        else:
            senha = input('Digite sua senha: ').upper().strip()
            indece = int(nomes.index(nome))#Saber o indece do nome, para confirmar senha.
            #print(type(senhas[indece]))
            if senha == senhas[indece].strip():
                print('\nBem vindo!, ' + nome + '\n')
                lista = [nome, senha]
                jogadores.append(lista)
            else:
                print('Senha incorreta!')
    return jogadores

def rodadas(jogadores,secreto,dicas):
    palpites = [] #tds os palpites recebe nome e palpite
    palpite_ = [] # recebe palpite//para saber qual o numero mais proximo
    vencedor = '' #nome vencedor
    palpite_vencedor = 0 #Valor proximo ou valor igual ao secreto
    for x in range(5):
        dica = random.choice(dicas) #pegar so uma dica entre as dicas
        dicas.pop(dicas.index(dica)) #Para retirar a dica já apresentada
        if x >= 1: #Mostrar dicas após a primeira rodada
            print(dica)
        for jogador in jogadores:#Para varrer a lista
            print(jogador[0])#O nome do jogador que vai dar o Palpite
            palpite = int(input('Qual o seu palpite: '))
            x = [jogador[0], palpite]
            palpites.append(x)
            if secreto > palpite:#Caso o secreto seja maior
                palpite_.append(secreto - palpite)
            else:#Secreto menor
                palpite_.append(palpite - secreto)
        for palpite in palpites:#Ver o vencedor ou quem chegou mais proximo.
            palpite_.sort()#Ordenar os palpites mais proximo
            if palpite[1] == secreto:#vencedor
                print('O jogador %s acertou' % palpite[0])
                break
            elif (palpite[1] - secreto) == palpite_[0]:#Palpite Proximo
                vencedor = palpite[0]
                palpite_vencedor = palpite[1]
            elif (secreto - palpite[1]) == palpite_[0]:#Palpite Proximo
                vencedor = palpite[0]
                palpite_vencedor = palpite[1]
    #print(palpite_)
    #print(palpite_[0])
    print('Vencedor: ',vencedor)
    print('Palpite: ',(palpite_vencedor))
    print('secreto: ',secreto)
    arquivo = open('vitorias.txt','a')#Adicionar o vencedor no arquivo
    arquivo.write(vencedor+'\n')
    arquivo.close()
    #print(palpites)

def rank():
    vencedores = []
    vecer = []
    arquivo = open('vitorias.txt', 'r')
    for linha in arquivo.readlines():
        a = linha.split()
        vecer.append(a)
    for v in vecer:
        #print(vecer.count(v))
        x = vecer.count(v)
        lista = [v, x]
        if lista not in vencedores:
            vencedores.append(lista)
    # print(vencedores)
    for l in vencedores:
        print('Nome %s venceu: %s vezes' % (''.join(l[0]), l[1]))
    arquivo.close()


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

    if secreto % 7 == 0:
        if 'O número é divisível por 7' not in dicas:
            dicas.append('O número é divisível por 7')

    if (secreto/2) < 26:
        if 'O número dividido por 2 e menor que a quantidade de letras do alfabeto' not in dicas:
            dicas.append('O número dividido por 2 e menor que a quantidade de letras do alfabeto')

    if secreto > 60:
        if 'O número e maior que a idade de BRASILIA DF' not in dicas:
            dicas.append('O número e maior que a idade de BRASILIA DF')
    else:
        if 'O número e menor que a idade de BRASILIA DF' not in dicas:
            dicas.append('O número e menor que a idade de BRASILIA DF')

    if secreto >= 1 and secreto < 1432:
        if 'O número está num intervalo de 1 e 1432' not in dicas:
            dicas.append("O número está num intervalo de 1 e 1432")


    if (secreto ** 1/2) > 32:
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
