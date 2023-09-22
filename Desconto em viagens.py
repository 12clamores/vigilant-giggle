valor_bruto = float(input("Informe o valor bruto da viagem:"))
categoria = input("Informe a categoria: ECONOMICA, EXECUTIVA ou PRIMEIRA CLASSE:")
quantidade_viajantes = int(input("Informe a quantidade de viajantes:"))
valor_desconto = 0
if categoria.upper() == "ECONOMICA":
    if quantidade_viajantes == 2:
        valor_desconto = valor_bruto * 0.03
    elif quantidade_viajantes == 3:
        valor_desconto = valor_bruto * 0.04
    elif quantidade_viajantes >= 4:
        valor_desconto = valor_bruto * 0.05
elif categoria.upper() == "EXECUTIVA":
    if quantidade_viajantes == 2:
        valor_desconto = valor_bruto * 0.05
    elif quatidade_viajantes == 3:
        valor_desconto = valor_bruto * 0.07
    elif quantidade_viajantes >= 4:
        valor_desconto = valor_bruto * 0.08
elif categoria.upper() == "PRIMEIRA CLASSE":
    if quantidade_viajantes == 2:
        valor_desconto = valor_bruto * 0.1
    elif quatidade_viajantes == 3:
        valor_desconto = valor_bruto * 0.15
    elif quantidade_viajantes >= 4:
        valor_desconto = valor_bruto * 0.2
else:
    print("Categoria inexistente não tera desconto")
valor_liquido = valor_bruto - valor_desconto
media_viajantes = valor_liquido / quantidade_viajantes
print(f"O valor da viagem é de R${valor_bruto} após o desconto de {valor_desconto} a viajem custara {valor_liquido} e cada passageiro tem o custo medio de {media_viajantes}")