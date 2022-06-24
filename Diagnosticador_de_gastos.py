def calc_perc(total, parte):
    perc = (parte * 100) / total
    return perc

def diagnosticador():
    renda = int(input("Renda mensal total: "))
    moradia = int(input("Gastos totais com moradia: "))
    educacao = int(input("Gastos totais com educacao: "))
    transporte = int(input("Gastos totais com transporte: "))

    tipo = [moradia,educacao,transporte]
    percentuais = []
    for cada in tipo:
        perc = round(calc_perc(renda, cada),2)
        percentuais.append(perc)

    max = [0.3, 0.2, 0.15]
    valor_maxList = []
    for cada in max:
        valor_max = round(renda * cada,2)
        valor_maxList.append(valor_max)

    if calc_perc(renda,moradia) > 30:
        mensagem0 = f"Portanto, idealmente, o maximo de sua renda comprometida com moradia deveria ser de R$ {valor_maxList[0]}"
    else:
        mensagem0 = "Seus gastos estao dentro da margem recomendada."
    if calc_perc(renda,educacao) > 20:
        mensagem1 = f"Portanto, idealmente, o maximo de sua renda comprometida com educacao deveria ser de R$ {valor_maxList[1]}"
    else:
        mensagem1 = "Seus gastos estao dentro da margem recomendada."
    if calc_perc(renda,transporte) > 15:
        mensagem2 = f"Portanto, idealmente, o maximo de sua renda comprometida com transporte deveria ser de R$ {valor_maxList[2]}"
    else:
        mensagem2 = "Seus gastos estao dentro da margem recomendada."

    # # # # #
    
    print("Diagnostico: ")
    print(f"Seus gastos totais com moradia comprometem {percentuais[0]}% de sua renda total. O maximo recomendado e de 30%. {mensagem0}")
    print(f"Seus gastos totais com educacao comprometem {percentuais[1]}% de sua renda total. O maximo recomendado e de 20%. {mensagem1}")
    print(f"Seus gastos totais com transporte comprometem {percentuais[2]}% de sua renda total. O maximo recomendado e de 15%. {mensagem2}")

diagnosticador()
