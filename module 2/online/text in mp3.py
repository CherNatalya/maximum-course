from pygame import mixer
from gtts import gTTS
file = open("text.txt", 'r', encoding='utf-8')
string = file.read()
file.close()
mixer.init()
tts = gTTS(text=string, lang='ru')
tts.save('text.mp3')
mixer.music.load('text.mp3')
mixer.music.play()
print(string)
