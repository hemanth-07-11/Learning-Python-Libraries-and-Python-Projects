import pyaudio
import speech_recognition as sr
import wave
import subprocess
from commands import Commander

running = True


def say(text):
    subprocess.call("PowerShell -Command Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('"+ text +"')", shell=True)

# Load auto files
def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()

    stream = pa.open(
        format=pa.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True
    )

    data_stream = wf.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    stream.close()
    pa.terminate()

# Instantiate Speech Recognition and Commander
r = sr.Recognizer()
cmd = Commander()


def init_speech():
    print("Listening...")
    play_audio('audio\R2D2-do.wav')             # Start listening
    
    with sr.Microphone() as source:             # Recoginzer listening though source (mic)
        print("Say something")
        audio = r.listen(source)

    play_audio('audio\R2D2-yeah.wav')           # Stop listening

    command = ""

    # Failsafe if recognizer not understand
    try:
        command = r.recognize_google(audio)    
    except:
        print("Could not understand")         

    print("Your command:" + command)         

    if command in ["quit", "cancel", "exit", "bye", "goodbye"]:
        global running
        running = False
    
    cmd.discover(command)                       #

while running == True:
    init_speech()
