def calculadora_ir(salario_bruto):
    #tabela de aliquotas e faixas de imposto de renda
    tabela_ir = [
        {"faixa": (0,1903.98), "aliquota": 0, "deducao": 0, },
        {"faixa": (1903,99,2826.65), "aliquota": 7.5, "deducao": 142, },
        {"faixa": (2826.65,3751.05), "aliquota": 15, "deducao": 354, },
        {"faixa": (3751.06,4667.68), "aliquota": 22.5, "deducao": 636, },
        {"faixa": (4667.69,float("inf")), "aliquota": 27.5, "deducao": 869, }
    ]

#calcular o imposto de renda
    resultado = 0
    valorAliquota = 0
    valorDeducao = 0

    for faixa in tabela_ir:
        if salario_bruto > faixa["faixa"][0]  and salario_bruto <= faixa["faixa"][1]:
            resultado = (salario_bruto * faixa["aliquota"]) / 100 - faixa["deducao"]
            valorAliquota = faixa["aliquota"]
            valorDeducao = faixa["deducao"]
            break
    return resultado, valorAliquota, valorDeducao



#testando nossa função

salario_bruto = float(input("informe o seu salário bruto: "))

resultado_final, valorAliquota, valorDeducao = calculadora_ir(salario_bruto)

salario_liquido = salario_bruto - resultado_final


print(f'O imposto de renda devido é R$ {resultado_final:.2f}')

print(f'aliquota aplicada é de R$ {valorAliquota}%')

print(f'deducao é de R$ {valorDeducao}')

print(f'O salário bruto é de R$ {salario_bruto}')



