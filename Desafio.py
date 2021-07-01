import Function
import random
num_jogadores = int(input('Quantos jogadores ira participar? '))
if num_jogadores >= 1 and num_jogadores <= 4:
    jogadores = Function.jogador(num_jogadores)
    print('''
    Este desafio tem o intuito de demonstrar como funciona um jogo no qual tem como princípio, 
    fazer com que os jogadores trabalhem a matemática, a história, raciocínio lógico e conhecimentos
     gerais ao tentar acertar um número gerado de forma aleatória
    ''')
    secreto = random.randrange(1,1000)
    dicas = Function.dica(secreto)
    Function.rodadas(jogadores, secreto,dicas)
else:
    print('Não permitimos essa quantidade de Participante!')