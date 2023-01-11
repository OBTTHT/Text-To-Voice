from typing import Text
from gtts import gTTS
import os


text = str(input("Metin Giriniz: "))

language = 'tr'

speech = gTTS(text = text, lang = language, slow = False)

speech.save("text.mp3")

os.system("start text.mp3")
