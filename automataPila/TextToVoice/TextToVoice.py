
from gtts import gTTS

class TextToVoice():

    def __init__(self, language):
        self._language = language

    def __init__(self) -> None:
        pass

    def createAudio(self, text, language, nameFile, nameFolder):
        audio = gTTS(text, lang = language)
        audio.save(f'automataPila/voice/{nameFolder}/{nameFile}.mp3')

    def getAudio(self, nameFile):
        pass

ad = TextToVoice()
ad.createAudio(
                'Chū: Parindorōmu no tango to wa, hidarikara migi ni, matawa sono gyaku ni onajiyōni yomu tangodesu.', 
                'es-us',
                'notaJap',
                'japanese'
               )

