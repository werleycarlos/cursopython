# Função para criar um carro com marca e  modelo
def criar_carro(marca, modelo):
    return{"marca": marca, "modelo": modelo}

# Função para acelerar o carro
def acelerar(carro):
    print(f"O {carro['marca']} {carro['modelo']} está acelerando.")

# Função para parar o carro
def parar(carro):
    print(f"O {carro['marca']} {carro['modelo']} parou.")

# Função virar para direita
def virar_direita(carro):
    print(f"O {carro['marca']} {carro['modelo']} viruou para direita.")

# Função virar para esquerda
def virar_esquerda(carro):
    print(f"O {carro['marca']} {carro['modelo']} viruou para esquerda.")

# Função para criar um carro com cor adicional
def criar_carro_com_cor(marca, modelo, cor):
    carro = criar_carro(marca, modelo) # cria um carro basico
    carro['cor'] = cor
    return carro

#exibir a cor do carro
def exibir_cor(carro):
    print(f"O carro é da cor {carro['cor']}.")
    

# criando os carros
carro1 = criar_carro("Fusca", "1984")
carro2 = criar_carro("Suzuki", "Jimmy")

#acelerando e parando
print(carro1["marca"]) #acessando a marca
print(carro1["modelo"]) #acessando o modelo

# criando um carro com cor
carro3 = criar_carro_com_cor("Toyota","Etios","Branco")
print(carro3['marca'])
print(carro3['modelo'])
print(carro3['cor'])
exibir_cor(carro3)

print("-------------------- Corrida --------------------------")
acelerar(carro3)

parar(carro3)

print(carro2["marca"])
print(carro2["modelo"])
acelerar(carro2)
virar_direita(carro2)
virar_esquerda(carro3)
parar(carro2)




