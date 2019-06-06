# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252
import urllib
import requests
import json
import telepot
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from cidades_fuzzy import *

    
bot = telepot.Bot('802597419:AAHGpYiYv-tV3k_5z9aPc-0C3sPdAz37LaA')

#Função que é chamada após o usuario clicar no botão
def on_callback_query(msg):
    global query_data
    query_id, from_id, query_data = telepot.glance(msg, flavor= 'callback_query')
    if query_data == "tempo_agora":
        bot.sendMessage(from_id, "Por favor, digite o nome da cidade desejada.")
    if query_data == "tempo_three_days":
        bot.sendMessage(from_id, "Por favor, digite o nome da cidade desejada.")

#Escuta a msg, e chama as funções
def rcv_msg(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    nome = msg['from']['first_name']
    if (msg['text'] == '/start'):
        bot.sendMessage(chat_id, f'Oi {nome}, muito prazer, sou o MR. Weather ou Sr. Tempo! Tô aqui pra te ajudar com o tempo em qualquer cidade do Brasil.')
        keyboard = InlineKeyboardMarkup(inline_keyboard = [ [InlineKeyboardButton(text = "Previsão do tempo hoje", callback_data = "tempo_agora")], [InlineKeyboardButton(text = "Previsão para os próximos 3 dias", callback_data = "tempo_three_days")] ] ) 
        bot.sendMessage(chat_id, "Em que posso te ajudar?", reply_markup=keyboard)
    texto = msg['text']
    texto = process.extract(texto, city, scorer=fuzz.token_sort_ratio)
    texto = list(texto[0])
    texto = texto[0]
    
    if query_data == 'tempo_agora':
        clima = pega_id(texto)
        pega_tempo_momento(clima, chat_id)
        
    elif query_data == 'tempo_three_days':
        clima = pega_id(texto)
        tempo_tres_dias(clima, chat_id)

#Função que pega o id na API pra usar outra vez
def pega_id(texto):
    climatempo = 'http://apiadvisor.climatempo.com.br/api/v1/locale/city?name=SãoPaulo&state=SP&token=9e6789cd36494206cef77f454694901a'
    city = ''
    state = texto[-2::]
    texto.replace(texto[-2::], '')
    for i in texto:
        if  i == '-':
            break
        else:
            city += i
    climatempo = climatempo[0:60] + city + climatempo[68:75] + state + climatempo[77:]
    clima = requests.get(climatempo).json()
    for i in clima:
        clima = (i['id'])
    return clima

#Função que retorna clima em tres dias
def tempo_tres_dias(clima, chat_id):
    clima = str(clima)
    url_tempo = 'http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/3477/days/15?token=9e6789cd36494206cef77f454694901a'
    url_tempo = url_tempo[:59] + clima + url_tempo[63:]
    tempo = requests.get(url_tempo)
    dados = json.loads(tempo.content)
    data = dados['data']
    seg_d = data[1]
    ter_d = data[2]
    quar_d = data[3]
    name = dados['name']
    state = dados['state']       

    for i in seg_d:
        date = seg_d['date_br']
        mini_dia = seg_d['temperature']['min']
        maxi_dia = seg_d['temperature']['max']
        chance_chuva = seg_d['rain']['probability']
        nasce_sol = seg_d['sun']['sunrise']
        por_sol = seg_d['sun']['sunset']

    nasce_sol = nasce_sol[:-3]
    por_sol = por_sol[:-3]
    bot.sendMessage(chat_id, f''' ---- Previsão para {name}-{state} ----
          ---- {date} ----''')
    bot.sendMessage(chat_id, f'''Temperatura mínima: {mini_dia}
Temperatura máxima: {maxi_dia}
Chance de chuva: {chance_chuva}%
Nascer do sol: {nasce_sol}
Pôr do sol: {por_sol}''')
    
    for i in ter_d:
        date = ter_d['date_br']
        mini_dia = ter_d['temperature']['min']
        maxi_dia = ter_d['temperature']['max']
        chance_chuva = ter_d['rain']['probability']
        nasce_sol = ter_d['sun']['sunrise']
        por_sol = ter_d['sun']['sunset']

    nasce_sol = nasce_sol[:-3]
    por_sol = por_sol[:-3]
    bot.sendMessage(chat_id, f' ---- Previsão para {date} ----')
    bot.sendMessage(chat_id, f'''Temperatura mínima: {mini_dia}
Temperatura máxima: {maxi_dia}
Chance de chuva: {chance_chuva}%
Nascer do sol: {nasce_sol}
Pôr do sol: {por_sol}''')
    
    for i in quar_d:
        date = quar_d['date_br']
        mini_dia = quar_d['temperature']['min']
        maxi_dia = quar_d['temperature']['max']
        chance_chuva = quar_d['rain']['probability']
        nasce_sol = quar_d['sun']['sunrise']
        por_sol = quar_d['sun']['sunset']

    nasce_sol = nasce_sol[:-3]
    por_sol = por_sol[:-3]        
    bot.sendMessage(chat_id, f' ---- Previsão para {date} ----')
    bot.sendMessage(chat_id, f'''Temperatura mínima: {mini_dia}
Temperatura máxima: {maxi_dia}
Chance de chuva: {chance_chuva}%
Nascer do sol: {nasce_sol}
Pôr do sol: {por_sol}''')

    bot.sendMessage(chat_id, "Fonte: Climatempo")
        


#Função que retorna o tempo no momento
def pega_tempo_momento(clima, chat_id):
    clima = str(clima)
    url_tempo = 'http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/3477/days/15?token=9e6789cd36494206cef77f454694901a'
    url_tempo = url_tempo[:59] + clima + url_tempo[63:]
    tempo = requests.get(url_tempo)
    dados = json.loads(tempo.content)
    data = dados['data']
    name = dados['name']
    state = dados['state'] 
    pri_d = data[0]
    
    for i in pri_d:
        date = pri_d['date_br']
        mini_dia = pri_d['temperature']['min']
        maxi_dia = pri_d['temperature']['max']
        chance_chuva = pri_d['rain']['probability']
        nasce_sol = pri_d['sun']['sunrise']
        por_sol = pri_d['sun']['sunset']
        
    nasce_sol = nasce_sol[:-3]
    por_sol = por_sol[:-3]
    bot.sendMessage(chat_id, f''' ---- Previsão para {name}-{state} ----
           ---- {date} ----''')
    bot.sendMessage(chat_id, f'''Temperatura mínima: {mini_dia}
Temperatura máxima: {maxi_dia}
Chance de chuva: {chance_chuva}%
Nascer do sol: {nasce_sol}
Pôr do sol: {por_sol}''')
    bot.sendMessage(chat_id, "Fonte: Climatempo")
    

bot.message_loop({'chat': rcv_msg, 'callback_query': on_callback_query})
