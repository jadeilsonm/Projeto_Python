while True:
    nome = input("nome: ").strip()
    if nome in (""," "):
        break
    else:
        nome_personagem = input("nome do seu personagem: ").strip()
        senha = input("senha:").strip()
        confimar_Senha = input("Confirmar senha:")
        if senha == confimar_Senha:
            print('')