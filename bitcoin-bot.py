import json
import ssl

import websocket


def vender():
    pass


def comprar():
    pass


def ao_abrir(ws):
    print('Abriu a conexão')

    json_subscribe ="""
{
    "event": "bts:subscribe",
    "data": {
        "channel": "live_trades_btcusd"
    }
}      
    
"""

    ws.send(json_subscribe)

def ao_fechar(ws):
    print('fechou a conexão')


def erro(ws,erro):
    print('Deu erro')
    print(erro)

def ao_mandar_mensagem(ws,mensagem):
    mensagem = json.loads(mensagem)
    price = mensagem['data']['price']
    print(price)

    if price > 8000:
        vender()
    elif price <7500:
        comprar()
    else:
        print('Aguardar')

if __name__ == '__main__':

    ws = websocket.WebSocketApp('wss://ws.bitstamp.net.',
                                on_open=ao_abrir,
                                on_close=ao_fechar,
                                on_error=erro,
                                on_message=ao_mandar_mensagem)

    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})




