import matplotlib.pyplot as plt

def exibir(x,y):
    plt.plot(x,y)
    plt.show()

def lerCSV(caminho):
    arquivo = open(caminho)
    conteudo = arquivo.read()
    arquivo.close()
    conteudo = conteudo.splitlines()
    rotulos = conteudo[0]
    rotulos = rotulos.split(',')
    conteudo = conteudo[1:]
    dados = []
  
    for linha in conteudo:
        linha = linha.split(',')
        dados.append(linha)

    return rotulos, dados

###############################

def pibEmAno():
    while True:
        rotulos, dados = lerCSV("PIBS.csv")

        anos = []
        for cada in dados:
            anos.append(cada[0])

        pais = input("Informe um pais: ")
        if not pais in rotulos:
            print("Pais nao disponivel.")
            break
        ano = input("Informe um ano entre 2013 e 2020: ")
        if not ano in anos:
            print("Ano nao disponivel.")
            break

        paisIndex = rotulos.index(pais)
        anoIndex = anos.index(ano)
        dadosDoAno = dados[anoIndex]
        pib = dadosDoAno[paisIndex]

        print(f"PIB {pais} em {ano}: US${pib} trilhoes.")
        break

pibEmAno()
print()


###############################

def pibAno(pais,ano):
        rotulos, dados = lerCSV("PIBS.csv")

        anos = []
        for cada in dados:
            anos.append(cada[0])

        paisIndex = rotulos.index(pais)
        anoIndex = anos.index(ano)
        dadosDoAno = dados[anoIndex]
        pib = float(dadosDoAno[paisIndex])

        return pib

##########################################################

def variacoesPib():
    rotulos, dados = lerCSV("PIBS.csv")
    rotulos = rotulos[1:]

    for pais in rotulos:
        pib2020 = float(pibAno(pais,"2020"))
        pib2013 = float(pibAno(pais,"2013"))
        variacao = round(((pib2020 - pib2013) * 100) / pib2013,2)

        print(f"{pais}: Variacao de {variacao}% entre 2013 e 2020.")

variacoesPib()
print()

####################################################

def graficoPibPais():
    rotulos, dados = lerCSV("PIBS.csv")
    pais = input("Informe um pais: ")

    anos = []
    for cada in dados:
        anos.append(cada[0])

    pibPorAno = []
    for cada in anos:
        cadaAno = pibAno(pais,cada)
        pibPorAno.append(cadaAno)
    
    anosInt = []
    for ano in anos:
        ano = int(ano)
        anosInt.append(ano)

    exibir(anosInt,pibPorAno)
        
graficoPibPais()