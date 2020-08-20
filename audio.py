import os
from gtts import gTTS
text = "Heyy Guys . This is Surajram here."

lang = 'en'
myobj = gTTS(text=text,lang = lang,slow=False)
myobj.save("audio.mp3")
os.system("audio.mp3")
