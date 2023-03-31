import speech_recognition as sr
from pytube import YouTube
import os
import whisper
model = whisper.load_model("base")


def create_and_open_txt(text, filename):
    with open(filename, "w") as file:
        file.write(text)
    os.startfile(filename)


url = input("Enter the YouTube video URL :")

yt = YouTube(url)

# text = yt.captions['a.en']


# .captions['en']
audio_stream = yt.streams.filter(only_audio=True).first()
filename = "audio.mp3"

audio_stream.download(filename=filename)

r = sr.Recognizer()

result = model.transcribe(filename)
print(result["text"])
# print(text)

# create_and_open_txt(text, "output.txt")
