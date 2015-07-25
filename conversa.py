#imports
import cmds
import json
import urllib
import urllib2
import logging

def responde(text):
    if 'who are you' in text:
        return('telebot starter kit, created by yukuku: https://github.com/yukuku/telebot')
    elif 'what time' in text:
        return('look at the top-right corner of your screen!')
    elif 'O que cai na prova' in text:
        return('Suas lagrimas')
    elif (text.find('quem')!=-1) and ((text.find('criou')!=-1) or (text.find('te')!=-1)) and ((text.find('voce')!=-1) or (text.find('bot')!=-1)):
        return('Fui criado pelo @bcesarg6 e o @cristoferoswald')
    else:
        try:
            resp1 = json.load(urllib2.urlopen('http://www.simsimi.com/requestChat?lc=en&ft=1.0&req=' + urllib.quote_plus(text.encode('utf-8'))))
            back = resp1.get('res')
        except urllib2.HTTPError, err:
            logging.error(err)
            back = str(err)
        if not back:
            return('okay...')
        elif 'I HAVE NO RESPONSE' in back:
            return('Voce fala de uma forma burra cara!')
        else:
            return(back)
