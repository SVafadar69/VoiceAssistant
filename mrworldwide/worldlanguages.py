from io import BytesIO
from translate import Translator
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
#from vlc import MediaPlayer
from pygame import mixer
from playsound import playsound
from vlc import MediaPlayer

from mysr import voice_to_text
from mysay import print_say
import wikipedia

# Convert text to speech in numerous languages

languages = {"english": 'en', "french": 'fr', "spanish": 'es', "chinese": "zh", "russian": 'ru'}


def mr_worldwide_mmm():
    global phrase, inp
    while True:
        print_say("What language would you like to translate")
        # inp = voice_to_text().lower()
        inp = input().lower()
        print_say(f"You said {inp}")

        print_say("What language would you like to translate to?")
        # translated_language = voice_to_text().lower()
        translated_language = input().lower()
        print_say(f" You said {translated_language}")

        machine_phrase = print_say("What phrase would you like to know")
        # phrase = voice_to_text().lower()
        phrase = input()
        print_say(f"You said {phrase}")

        # Obtain answer from Wikipedia and print it out
        wikipedia.set_lang(languages[inp])
        ans = wikipedia.summary(phrase[:100])  # prints first 100 words
        #print_say(ans)

        # Capture spoken English
        # Specify the input and output languages
        translator = Translator(from_lang=languages[inp], to_lang=languages[translated_language])

        # Do the actual translation
        translation = translator.translate(phrase)
        print_say(translation)

        # Convert text to speech in Spanish
        tts = gTTS(text=translation, lang=languages[translated_language])

        # Create a temporary file
        voice = BytesIO()

        # Save the voice output as an audio file
        tts.write_to_fp(voice)

        # Play the audio file

        #
        voice.seek(0)
        # play(AudioSegment.from_mp3(voice))

        mediaplayer = MediaPlayer()
        mediaplayer(voice)
        mediaplayer.play()

mr_worldwide_mmm()
