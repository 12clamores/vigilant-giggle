idade = int(input("Informe sua idade:"))
bpm = int(input("Informe seus batimentos cardíacos:"))
if idade <= 2:
    if bpm >= 120 and bpm <= 140:
        print("Esta dentro da faixa adequada")
    else:
        print("Esta acima da faixa adequada")
elif idade >=8 and idade <=17:
    if bpm >=80 and bpm <=100:
        print("Esta dentro da faixa adequada")
    else:
        print("Esta acima da faixa adequada")
elif idade >=18 and idade <=60:
    if bpm >= 70 and bpm <=80:
        print("Frequência cardíaca dentro da faixa adequada")
    else:
       print("Frequência cardíaca acima da faixa adequada")
else:
    print("frequência cardíaca a baixo da faixa adequada")

