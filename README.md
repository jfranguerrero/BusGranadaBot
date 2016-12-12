# BusGranadaBot
[![Heroku Deploy](https://www.herokucdn.com/deploy/button.svg)](https://busgranadabot.herokuapp.com/)

## Descripción del proyecto

Bot para Telegram desarrollado en Python cuya finalidad es la de obtener y mostrar al usuario el tiempo restante de los autobuses urbanos de Granada para llegar a una determinada parada.

Se le indicará una parada y éste responderá con el tiempo restante de todas las líneas que se detengan en dicha parada.

## Instalación

Lo primero es descargar todos los ficheros necesarios para el funcionamiento del bot. Esto se realiza mediante:

```
git clone https://github.com/jfranguerrero/BusGranadaBot.git
```

Realizado esto necesitaremos instalar las dependencias ubicadas en el fichero requirements.txt. Esto lo llevará a cabo automáticamente el Makefile

```
make install
```
Finalmente antes de ejecutar el bot necesitaremos un token el cual nos lo proporcionará el usuario [@BotFather](https://telegram.me/BotFather)

Cuando lo tengamos creamos una variable de entorno con él:

```
export token_busbot='XXX'
```

Donde 'XXX' será el token proporcionado por Telegram.

Para lanzar el bot:

```
make execute
```

## funcionamiento

Simplemente se deberá introducir el número de parada y el bot se encargará de devolver un mensaje con los tiempos restantes.

Puede verse el bot en funcionamiento en el siguiente enlace : https://telegram.me/BusGranadaBot

## Adicional

Se incluye el fichero Procfile para que el bot pueda ser desplegado automáticamente en Heroku si es necesario.
