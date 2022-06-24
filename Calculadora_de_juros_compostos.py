import matplotlib.pyplot as plt

def exibirGrafico(x,y):
    plt.plot(x,y)
    plt.show()

def calculadora():
    montante = float(input("Valor inicial: R$"))
    juro = float(input("Rendimento por periodo (%): ")) / 100
    aporte = float(input("Aporte a cada periodo: R$"))
    periodos = int(input("Total de periodos: "))
    todosMontantes = []
    numPeriodo = []
    num = 1

    for x in range(1,periodos + 1):
        montante = ((montante + montante * juro) + aporte)
        print(f"Apos {x} periodo(s), o montante sera de R${round(montante,2)}")
        todosMontantes.append(montante)
        num += 1
        numPeriodo.append(num)

    exibirGrafico(numPeriodo,todosMontantes)

calculadora()

