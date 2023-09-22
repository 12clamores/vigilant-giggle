idade = int(input("Informe sua idade:"))
bpm = int(input("Informe seus batimentos cardíaco:"))
if idade <= 2:
    if bpm >=120:
        if bpm <=140:
            print("Esta dentro da faixa adequada")
        else:
            print("Esta acima da faixa adequada")
    else:
            print("Esta a baixo da faixa adequada")
elif idade >=8:
    if idade <=17:
        if bpm >=80:
            if bpm <=100:
                print("Esta dentro da faixa adequada")
            else:
                print("Esta acima da faixa adequada")
        else:
            print("Esta a baixo da faixa adequada")
    if idade >=18:
        if idade <=60:
            if bpm >=70:
                if bpm <=80:
                    print("Esta dentro da faixa adequada")
                else:
                    print("Esta acima da faixa adequada")
            else:
                print("Esta a baixo da faixa adequada")
        else:
            if bpm >=50:
                if bpm <=60:
                    print("Esta dentro da faixa adequada")
                else:
                    print("Esta acima da faixa adequada")
            else:
                print("Esta a baixo da faixa adequada")
else:
    print("Não foi possível verificar os batimentos para essa idade")
