# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela


from datetime import datetime, timedelta

starter_date = datetime(2020,12,20)

value = 1000000
time_years = 5
quotas = time_years * 12
quota_value = value/quotas
end_year = starter_date.year + time_years
end_date = datetime(end_year,12,20)
quota = 1

date = starter_date

while date != end_date:
    date += timedelta(days = 1)
    if date.day == 20:
        date_format = '%d-%m-%Y'
        formated_date = date.strftime(date_format)
        print(f"{quota} - {formated_date} - R${round(quota_value,2)}")
        quota += 1



"""
solção do professor
from datetime import datetime

from dateutil.relativedelta import relativedelta

valor_total = 1_000_000
data_emprestimo = datetime(2020, 12, 20)
delta_anos = relativedelta(years=5)
data_final = data_emprestimo + delta_anos

data_parcelas = []
data_parcela = data_emprestimo
while data_parcela < data_final:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)

numero_parcelas = len(data_parcelas)
valor_parcela = valor_total / numero_parcelas

for data in data_parcelas:
    print(data.strftime('%d/%m/%Y'), f'R$ {valor_parcela:,.2f}')

print()
print(
    f'Você pegou R$ {valor_total:,.2f} para pagar '
    f'em {delta_anos.years} anos '
    f'({numero_parcelas} meses) em parcelas de '
    f'R$ {valor_parcela:,.2f}.'
)



"""
