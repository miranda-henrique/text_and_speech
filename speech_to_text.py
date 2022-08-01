import speech_recognition as sr
from gtts import gTTS
import os
from datetime import datetime
import playsound
import pyjokes
import wikipedia
import pyaudio
import webbrowser
import winshell
from pygame import mixer


#get mic audio
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        # wait for a second to let the recognizer adjust the
        # energy threshold based on the surrounding noise level
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio, language='pt-BR')
            print(said)
        except sr.UnknownValueError:
            speak("Desculpe, não entendi.")
        except sr.RequestError:
            speak("Desculpe, esta função não está disponível no momento.")
    return said.lower()

#speak converted audio to text
def speak(text):
    tts = gTTS(text=text, lang='pt-BR')
    filename = "voice.mp3"
    try:
        os.remove(filename)
    except OSError:
        pass
    tts.save(filename)
    playsound.playsound(filename)

#function to respond to commands
def respond(text):
    print("Texto obtido do áudio " + text)
    if 'youtube' in text:
        speak("O que deseja buscar?")
        keyword = get_audio()
        if keyword!= '':
            url = f"https://www.youtube.com/results?search_query={keyword}"
            webbrowser.get().open(url)
            speak(f"Here is what I have found for {keyword} on youtube")
    elif 'buscar' or 'busca' or 'busque' or 'pesquisa' or 'pesquise' in text:
        speak("Qual assunto deseja buscar?")
        query = get_audio()
        if query !='':
            result = wikipedia.summary(query, sentences=3)
            speak("De acordo com a wikipédia")
            print(result)
            speak(result)
    elif 'piada' in text:
        speak(pyjokes.get_joke())
    elif 'esvaziar lixeira' in text:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
        speak("Lixeira esvaziada")
    elif 'que horas' in text:
        strTime = datetime.today().strftime("%H:%M %p")
        print(strTime)
        speak(strTime)
    elif 'tocar' or 'música' in text or 'tocar música' in text:
        speak("Tocando...")
        music_dir = "C:\\Users\\UserName\\Downloads\\Music\\" #add your music directory here..
        songs = os.listdir(music_dir)
        #counter = 0
        print(songs)
        playmusic(music_dir + "\\" + songs[0])
    elif 'parar música' in text:
        speak("Interrompendo música.")
        stopmusic()
    elif 'sair' in text:
        speak("Até a próxima.")
        exit()
#play music
def playmusic(song):
    mixer.init()
    mixer.music.load(song)
    mixer.music.play()
#stop music
def stopmusic():
    mixer.music.stop()

#let's try it
#text = get_audio()
#speak(text)
while True:
    print("Estou ouvindo...")
    text = get_audio()
    respond(text)
