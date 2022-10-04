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

            #devolver pedido
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

