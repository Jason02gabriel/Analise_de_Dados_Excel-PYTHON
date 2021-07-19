import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC1bbe502d6c3c6544a92730094052a875"
# Your Auth Token from twilio.com/console
auth_token = "dc53156be5e27d7598f14ef353a61f54"

#Abrir os 6 arquivos em excel
lista_meses= ['janeiro','fevereiro','março','abril','maio','junho']
#para cada arquivo:
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    # veriicar se algum valor na coluna vendar é maior que 55.000
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000 , 'Vendas'].values[0]
        # se for maior que 55.000 enviar um sms com o nome , mês e as venas do vendedor


        client = Client(account_sid,auth_token)
        message = client.messages.create(
            to="+5586999527162",
            from_="+15033609393",
            body=f"no mês de {mes} o vendedor {vendedor} fez {vendas} vendas")

        print(message.sid)





