# -*- coding: utf-8 -*-
import sys
import telebot # Librería de la API del bot.
from telebot import types # Tipos para la API del bot.
import time
from bs4 import BeautifulSoup
import requests
import os

reload(sys)
sys.setdefaultencoding('utf8')


TOKEN =os.environ['token_busbot']   #pasamos el token como variable de entorno

bot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.

def listener(messages):
    for m in messages:
        if m.content_type == 'text': #  mensajes que sean tipo texto.
            cid = m.chat.id # Almacenaremos el ID de la conversación.
            print "[" + str(cid) + "]: " + m.text
            if (m.text.isnumeric()):
                url="http://transportesrober.com:9055/websae/Transportes/parada.aspx?idparada=%s"%m.text    #URL con la parada a consultar

                req = requests.get(url) #Realizamos la petición

                statusCode = req.status_code
                if statusCode == 200: #Comprobamos que se realizó correctamente la petición
                    soup = BeautifulSoup(req.text, "lxml")  #Creamos una araña que rastree el documento obtenido con la petición
                    entradas = soup.find('td',{'class':'tablacabecera'}).getText()  #Extraemos el nombre de la parada
                    if(entradas=='Error'):  #Si el nombre es error es que la parada no existe
                        bot.send_message(cid, "Error, no existe la parada introducida.")
                    else:
                        entradas+="\n\n"    #Añadimos un salto de línea para separar el nombre de la parada de los tiempos
                        datos = soup.find_all('td', {'class' : 'tabla_campo_valor'})   #Extraemos las líneas y sus tiempos. Luego eliminaremos el destino de linea que también se extrae
                        if(len(datos)<3):   #Si el vector obtenido es menor de 3 es que no hay ninguna línea acercándose a la parada
                            entradas+="No hay autobuses acercándose"    #Indicamos que no hay autobuses
                            bot.send_message(cid, entradas)             #Enviamos el mensaje al usuario
                        else:
                            i=0
                            salto_doble=True
                            while i < len(datos):           #Recorremos el vector con los datos
                                out=datos[i].getText()
                                out=out.strip('\t\r\n')     #Eliminamos tabulaciones y saltos de líneas sobrantes de los datos

                                if(salto_doble):            #Indicamos mediante el booleano salto_doble que se salte los elementos donde están los destinos
                                    i+=2
                                    salto_doble=False
                                    entradas+="Línea: "+out+"\t"    #Añadimos al string que se mostrará la línea

                                else:
                                    i+=1
                                    salto_doble=True
                                    if (len(out)==0):       #Si el tamaño del elemento del tiempo es 0 significa que es inminente
                                        entradas+="Tiempo: Inminente"
                                    else:
                                        entradas+="Tiempo: "+out+ " minutos"
                                    entradas=entradas+"\n\n"

                            bot.send_message(cid, entradas)
                else:
                    bot.send_message(cid, "Error al comprobar los horarios.")
            elif(m.text=='/start'):
                bot.send_message(cid, 'Bienvenido a BusGranadaBot. Podrás saber el tiempo restante de los autobuses de tu parada simplemente con introducir el número de parada.')
            else:
                bot.send_message(cid, 'Lo siento, debe introducir el número de parada de forma correcta.')

bot.set_update_listener(listener) # Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba.





bot.polling(none_stop=True) # Con esto, le decimos al bot que siga funcionando incluso si encuentra algún fallo.
