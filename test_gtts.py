from gtts import gTTS
import os

text = "Voici mon premier test de synthèse vocale. Mais, est ce que cela fonctionne ?"
tts = gTTS(text=text, lang='fr')
tts.save("test.mp3")
os.system("mpg123 test.mp3")
