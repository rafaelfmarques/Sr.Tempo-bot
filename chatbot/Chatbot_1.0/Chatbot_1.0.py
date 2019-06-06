# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

import urllib
import requests
import json
import telepot
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

try: FileNotFoundError
except NameError:
    import sys
    if sys.version_info < (3,0):
        reload(sys)
        sys.setdefaultenconding('utf-8')
    FileNotFoundError = IOError
    
bot = telepot.Bot('802597419:AAHGpYiYv-tV3k_5z9aPc-0C3sPdAz37LaA')
      

def rcv_msg(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    from_id = telepot.glance(msg)
    nome = msg['from']['first_name']
    while True:
        bot.sendMessage(chat_id, f'Oi {nome}, muito prazer, sou o MR. Weather ou Sr. Tempo! Eu existo para te mandar a situação do tempo em qualquer cidade do Brasil.')
        keyboard = InlineKeyboardMarkup(inline_keyboard = [ [InlineKeyboardButton(text = "Previsão do tempo no momento", callback_data = "tempo_agora")], [InlineKeyboardButton(text = "Previsão para 3 dias", callback_data = "tempo_three_days")] ] ) 
        bot.sendMessage(chat_id, "Em que posso te ajudar?", reply_markup=keyboard)
        if (msg['text']):
            break
    texto = msg['text']
    chat_id = msg['from']['id']
    pega_id(texto, chat_id, msg)

def pega_id(texto, chat_id, msg):
    climatempo = 'http://apiadvisor.climatempo.com.br/api/v1/locale/city?name=São Paulo&state=SP&token=9e6789cd36494206cef77f454694901a'
    city = ''
    state = texto[-2::]
    texto.replace(texto[-2::], '')
    for i in texto:
        if  i == '-':
            break
        else:
            city += i
    climatempo = climatempo[0:60] + city + climatempo[69:76] + state + climatempo[78:]
    clima = requests.get(climatempo).json()
    for i in clima:
        clima = (i['id'])
    pega_tempo_momento(clima, chat_id)
    pega_tempo_three_days(clima, chat_id)

def pega_tempo_three_days(clima, chat_id):
    clima = str(clima)
    url_tempo: 'http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/3477/hours/72?token=http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/3477/hours/72?token=9e6789cd36494206cef77f454694901a'
    url_tempo = url_tempo[:58] + clima + url_tempo[62:]
    tempo = requests.get(url_tempo)
    dados = json.loads(tempo.content)
    
def pega_tempo_momento(clima, chat_id):
    clima = str(clima)
    url_tempo = 'http://apiadvisor.climatempo.com.br/api/v1/weather/locale/3477/current?token=9e6789cd36494206cef77f454694901a'
    url_tempo = url_tempo[:58] + clima + url_tempo[62:]
    tempo = requests.get(url_tempo)
    dados = json.loads(tempo.content)
    nome, estado, temperatura, velocidade_vento, situacao, umidade, sensacao, data =(
        (dados['name']), (dados['state']),(dados['data']['temperature']),(dados['data']['wind_velocity']), (dados['data']['condition']),
        (dados['data']['humidity']), (dados['data']['sensation']), (dados['data']['date']))

    
    if umidade < 12:
        emerg = "ESTADO DE EMERGÊNCIA! EVITE QUALQUER ATIVIDADE FÍSICA ENTRE 10 E 16 HORAS!"
    if umidade < 20:
        emerg = "ESTADO DE ALERTA! EVITE ATIVIDADES FÍSICAS ENTRE 10 E 16 HORAS!"
    if umidade < 30:
        emerg = "ESTADO DE ATENÇÃO! EVITE ATIVIDADES FÍSICAS ENTRE AS 11 E 15 HORAS!"
    if umidade < 60:
        emerg = "CUIDADO. UMIDADE ABAIXO DO IDEAL"
    else:
        emerg = "UMIDADE DO AR PROPÍCIO PARA REALIZAR ATIVIDADES FÍSICAS."
    bot.sendMessage(chat_id, f'{nome}-{estado} no momento está com {temperatura}ºC, com sensação de {sensacao}ºC. {situacao} e com umidade em {umidade}%. {emerg}')
    bot.sendMessage(chat_id, f'Atualizado em: {data}')
    
def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor= 'callback_query')
    if query_data == "tempo_agora":
        bot.sendMessage(from_id, "Por favor, digite o nome da cidade desejada. EX: São Paulo-SP")
    if query_data == "tempo_three_days":
        bot.sendMessage(from_id, "Por favor, digite o nome da cidade desejada para ver a previsão em 3 dias. EX: São Paulo-SP")

bot.message_loop({'chat': rcv_msg, 'callback_query': on_callback_query})

while True:
   pass
