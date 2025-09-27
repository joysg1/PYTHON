from gtts import gTTS
import io
import pygame

pygame.init()
pygame.mixer.init()

texto = "Hola, esto es un ejemplo de texto a voz."
tts = gTTS(text=texto, lang='es')

fp = io.BytesIO()
tts.write_to_fp(fp)
fp.seek(0)

pygame.mixer.music.load(fp)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

