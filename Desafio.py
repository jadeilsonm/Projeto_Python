import Function #Funçoes criadas
import random
while True: #Rodar infinitas vezes ate o usuario não quiser mais.
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

        print('''
        
    Deseja jogar novamente?
    1 - Sim
    2 - Não
        
        ''')
        opcao = int(input())
        if opcao == 2:
            print('''
            
    Deseja o Rank de vencedores?
    1 - Sim
    2 - Não
            
            ''')
            opcao = int(input())
            if opcao == 1:
                Function.rank()
                print('Fim de jogo!')
                break
            elif opcao == 2:
                print('Fim de jogo!')
                break
    else:
        print('Não permitimos essa quantidade de Participante!')
        break