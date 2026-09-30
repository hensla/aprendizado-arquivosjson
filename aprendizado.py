with open("clientes.txt", "w") as arquivo0:
    arquivo0.write("111, João, 989.23, 345.54\n222, Maria, 758.32, 549.07\n333, Ana, 495.65, 568.12\n444, Paulo, 533.54, 965.02")


with open("clientes.txt", "r") as arquivo:
    cli = {} #dicionario

    for i in arquivo: #i = linha
        dados = i.split(", ") #dados = lista heterogenea
        cod = dados[0]
        nome = dados[1]
        compras = [float(dados[2]), float(dados[3])]
        cli[cod] = {"nome": nome, "compras": compras} #cli = chave [cod] = identificador
        print(f'codigo: {cod} {cli[cod]}')
