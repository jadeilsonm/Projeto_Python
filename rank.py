vencedores = []
vecer = []
arquivo = open('vitorias.txt','r')
for linha in arquivo.readlines():
    a = linha.split()
    vecer.append(a)
for v in vecer:
    print(vecer.count(v))
    x = vecer.count(v)
    lista = [v, x]
    if lista not in vencedores:
        vencedores.append(lista)
#print(vencedores)
for l in vencedores:
    print('Nome %s venceu: %s vezes' % (''.join(l[0]), l[1]))
arquivo.close()
