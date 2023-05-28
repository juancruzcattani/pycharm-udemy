import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
import pyaudio


#escuchar nuestro microfono y devolver audio en texto

def transformar_audio_en_texto():
    #almacenar recognizer en variable

    r = sr.Recognizer()

    #configurar el micrfono
    with sr.Microphone() as origen:

        #tiempo de delay
        r.pause_threshold = 0.8

        # informar que comenzo la grabacion
        print("Ya puedes hablar!")

        #guardar audio
        audio = r.listen(origen)

        try:
            # buscar en google lo que haya escuchado
            pedido = r.recognize_google(audio, language="es-ar")

            #prueba de ingreso
            print("Dijiste: " + pedido)

            #devolver pedido
            return pedido

        # en caso de que no comprenda el audio
        except sr.UnknownValueError:

            #prueba de que no comprendio el audio
            print("Ups, no entendi lo dicho")

            #devolver error
            return "Sigo esperando"
        #en caso de no poder resolver el pedido
        except sr.RequestError:

            # prueba de que no comprendio el audio
            print("Ups, no entendi lo dicho")

            # devolver error
            return "Sigo esperando"
        #error inesperado
        except:
            # prueba de que no comprendio el audio
            print("Ups, algo ha salido mal")

            # devolver error
            return "Vuelve a internarlo"

#funcino para que el asistente pueda ser escuchado

def hablar(mensaje):

    #encender el motor de pyttsx3
    engine = pyttsx3.init()

    #pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


hablar("Hola mundo")

