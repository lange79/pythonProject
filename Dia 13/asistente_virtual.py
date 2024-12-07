import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
from wikipedia import languages

# opciones de voz /idioma
id1="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0"
id2="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
id3="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0"

# escuchar microfono y devolver como texto
def transformar_audio_en_texto():
    # almacenar recognizer en variable
    r=sr.Recognizer()

    # configurar el microfono
    with sr.Microphone() as origen:

        #tiempo de espera
        r.pause_threshold = 0.8

        # informar que comenzo la grabacion
        print("Ya puedes hablar")

        # guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            # buscar en goole
            pedido = r.recognize_google(audio, language="es-ar")

            # prueba de que pudo ingresar
            print("Dijiste:" + pedido)

            # devolver pedido
            return  pedido

        # en caso de que no comprenda el audio
        except sr.UnknownValueError:

            # prueba de que no comprendio el audio
            print("Ups, no entendi")

            # devolver error
            return "Sigo esperando"

        # en caso de no resolver el pedido
        except sr.RequestError:

            # prueba de que no comprendio el audio
            print("Ups, no entendi")

            # devolver error
            return "Sigo esperando"

        # error inesperado
        except:

            # prueba de que no comprendio el audio
            print("Ups, algo ha salido mal")

            # devolver error
            return "Sigo esperando"


# Funcion para que el asistente pueda ser escuchado
def hablar(mensaje):

    # encender el motor pyttsx3
    engine = pyttsx3.init()
    engine.setProperty("voice", id1)

    #Pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()



#############################Prueba de voces en el sistema###############################
"""engine = pyttsx3.init()
for voz in engine.getProperty("voices"):
    print(voz)"""
#########################################################################################

# informar dia de la semana
def pedir_dia():
    #Crear variable con datos de hoy
    dia=datetime.date.today()
    print(dia)

    # Crear variable para el dia de la semana
    dia_semana = dia.weekday()
    print(dia_semana)

    # Diccionario con nombre de dias
    calendario = {0:"Lunes",
                  1:"Martes",
                  2:"Miercoles",
                  3:"Jueves",
                  4:"Viernes",
                  5:"Sabado",
                  6:"Domingo"}

    # Decir dia de la semana
    hablar(f"Hoy es {calendario[dia_semana]}")


# Imformar la hora
def pedir_hora():

    # Crear una variable con datos de la hora
    hora = datetime.datetime.now()
    hora=f"En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos"
    print(hora)

    # decir la hora
    hablar(hora)


def saludo_inicial():

    # crear variable con dato de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = "Buenas noches"
    elif 6 <= hora.hour < 13:
        momento = "Buen dia"
    else:
        momento = "buenas tardes"

    # decir el saludo
    hablar(f"Hola, {momento}. soy Elena, tu asistente personal. Por favor dime en que te puedo ayudar")


# funcion central del asistente

def pedir_cosas():

    # activar el saludo inicial
    saludo_inicial()

    # variable de corte
    comenzar = True

    # loop central

    while comenzar:

        # activar el microfono y guardar el pedido en un string
        pedido = transformar_audio_en_texto().lower()

        if "abrir youtube" in pedido:
            hablar("Con gusto, estoy abriendo Youtube")
            webbrowser.open("https://www.youtube.com")
            continue
        elif "abrir navegador in pedido":
            hablar("Claro, estoy en eso")
            webbrowser.open("https://google.com")
            continue

        elif "que dia es hoy" in pedido:
            pedir_dia()
            continue
        elif "que hora es" in pedido:
            pedir_hora()
            continue
        elif "buscar en wikipedia" in pedido:
            hablar("buscando en wikipedia")
            pedido = pedido.replace("wikipedia", "")
            wikipedia.set_lang("es")
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar("Wikipedia dice lo siguiente:")
            hablar(resultado)
            continue

        elif "busca en internet" in pedido:
            hablar("Ya estoy en eso")
            pedido = pedido.replace("busca en internet", "")
            pywhatkit.search(pedido)
            hablar("Esto es lo que he encontrado")
            continue
        elif "reproducir" in pedido:
            hablar("buena idea, ya comienzo a reproducirlo")
            pywhatkit.playonyt(pedido)
            continue
        elif "broma" in pedido:
            hablar(pyjokes.get_joke("es"))
            continue
        elif "precio de las acciones" in pedido:
            accion= pedido.split("de")[-1].strip()
            cartera= {"apple":"APPL",
                      "amazon":"AMZN",
                      "google":"GOOGL"}

            try:
                accion_buscada= cartera[accion]
                accion_buscada=yf.ticker(accion_buscada)
                precio_actual = accion_buscada.info["regularMarketPrice"]
                hablar(f"La encontre, el precio de {accion} es {precio_actual}")
                continue
            except:
                hablar("Perdon, pero no la he encontrado")
                continue

        elif "adiós" in pedido:
            hablar("Mevoy a descansar, cualquier cosa me avisas")
            break

pedir_cosas()




