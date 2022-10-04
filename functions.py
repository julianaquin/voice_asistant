import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia


# escuchar nuestro microfono y devolver el audio como texto
def transformar_audio_en_texto():

    # almacenar recognizer en variable
    r = sr.Recognizer()

    # configurar el microfono
    with sr.Microphone() as origen:

        # tiempo de espera
        r.pause_threshold = 0.8

        # informar que comenzo la grabación
        print('ya puedes hablar')

        # guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            # buscar en google
            pedido = r.recognize_google(audio, language="es-co")

            # prueba que pudo ingresar
            print("dijiste: " + pedido)

            # devolver pedido
            return pedido
        # en caso de que no comprenda el audioop
        except sr.UnknownValueError:

            # Prueba de que no comprendio el audio
            print('ups, no entendi')

            # devolver error
            return "sigo esperando"

        # en caso de no poder convertir el pedido a string
        except sr.RequestError:

            # prueba de que no comprendio el audio
            print('ups, no hay servicio')

            # devolver error
            return "sigo esperando"

        # error inesperado
        except:

            # prueba de que no comprendio el audio
            print('ups, algo ha salido mal')

            # devolver error
            return "sigo esperando"


# funcion para que el asistente pueda ser escuchado
def hablar(mensaje):

    # encender el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id2)

    # pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


# informar el dia de la semana
def pedir_dia():

    # crear variable con datos de hoy
    dia = datetime.date.today()
    print(dia)

    # crar una variable para el dia de semana
    dia_semana = dia.weekday()
    print(dia_semana)

    # diccionario con nombre de los dias
    calendario = {0: 'Lunes',
                  1: 'Martes',
                  2: 'Miércoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sábado',
                  6: 'Domingo'}

    # decir el dia de la semana
    hablar(f'Hoy es {calendario[dia_semana]}')


# informar que hora es
def pedir_hora():

    # crear una variable con datos de la hora
    hora = datetime.datetime.now()
    hora2 = f'En este momento son las {hora.hour} con {hora.minute} minutos y {hora.second} segundos '
    print(hora)
    hablar(hora2)


# funcion saludo inicial
def saludo_inicial():

    # crear variable con datos de hora
    hora = datetime.datetime.now()
    print(hora)
    if hora.hour > 6 or hora.hour > 23:
        momento = 'Buenas noches'
    elif 6 <= hora.hour < 13:
        momento = 'Buenos dias'
    else:
        momento = 'Buenas tardes'

    # saludar
    hablar(f'{momento} soy Julianito, su asistente personal. porfavor dime en que te puedo ayudar.')
