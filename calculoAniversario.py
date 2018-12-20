import mod_diferenca_datas
from datetime import date

print('Olá, seja bem vindo ao programa calcula aniversário.')
print('Se você é como eu e vive esquecendo quantos anos tem, você está no programa certo :)')

print('Para começar digite abaixo:')
dia = input("Qual o seu dia de aniversário? (Ex: 3)")

while not dia.isnumeric() or int(dia) > 31:
    print("Somente números válidos meu amigaum")
    dia = input("Qual o seu dia de aniversário? (Ex: 3)")

mes = input("Qual o seu mês de aniversário? (Ex: 6)")
while not mes.isnumeric() or int(mes) > 12:
    print("Somente números válidos meu amigaum")
    mes = input("Qual o seu mês de aniversário? (Ex: 6)")

ano = input("Qual o ano em que você nasceu? (Ex: 1983)")
while not ano.isnumeric() or (int(ano) < 1900 or int(ano) > int(date.today().year)):
    print("Somente números válidos meu amigaum")
    ano = input("Qual o ano em que você nasceu? (Ex: 1983)")

print("Muito bem, você nasceu em {}/{}/{}".format(dia, mes, ano))

diferenca_datas_dias = mod_diferenca_datas.diferenca_dias(dia, mes, ano)
diferenca_datas_anos = mod_diferenca_datas.diferenca_anos(dia, mes, ano)

print("Parabéns, você tem {} anos, e está vivendo a {} dias!".format(diferenca_datas_anos, diferenca_datas_dias))
