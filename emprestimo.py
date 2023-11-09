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





