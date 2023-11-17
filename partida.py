def calculo_nv(vitorias, derrotas):
    saldo_vitorias = vitorias - derrotas

    if saldo_vitorias <= 10:
        nivel = 'Ferro'
    elif 11 <= saldo_vitorias <= 20:
        nivel = 'Bronze'
    elif 21 <= saldo_vitorias <= 50:
        nivel = 'Prata'
    elif 51 <= saldo_vitorias <= 80:
        nivel = 'Ouro'
    elif 81 <= saldo_vitorias <= 90:
        nivel = 'Diamante'
    elif 91 <= saldo_vitorias <= 100:
        nivel = 'Lendário'
    else:
        nivel = 'Imortal'

    return saldo_vitorias, nivel

vitorias = 500
derrotas = 10
saldo_vitorias, nivel = calculo_nv(vitorias, derrotas)


print(f"O herói tem saldo de {saldo_vitorias} e está no nível {nivel}")
