from gtts import gTTS
from langdetect import detect
from constants import LANGUAGES_REVERSED

text = ''
language = ''
languages_reversed = LANGUAGES_REVERSED


def text_to_speech(input_text: str, input_language: str):
    gtts_object = gTTS(text=input_text,
                       lang=input_language,
                       slow=False)

    gtts_object.save("gtts.wav")

    print('Texto convertido para áudio salvo em gtts.wav')


###################################################################

def get_text_and_language():
    print('\nInsira um texto para ser convertido para fala: ')
    text = input()

    language_is_correct = '0'

    while language_is_correct == '0':
        language = detect(text)
        full_language = languages_reversed.get(language)

        print(f'\nO idioma é {full_language}? \n0 - Não \n1 - Sim')
        language_is_correct = input()

        if language_is_correct != '0' and language_is_correct != '1':
            print('Insira uma opção válida')

    return text, language


text, language = get_text_and_language()
text_to_speech(text, language)
