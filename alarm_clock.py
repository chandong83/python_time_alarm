import datetime
import pygame
import time

pygame.init()

audio_volume = 0.5
audio_interval = 1

sound = pygame.mixer.Sound('alarmaudio/start.wav')
print('{0}'.format(sound.get_volume()))
sound.set_volume(audio_volume)
sound.play()
time.sleep(audio_interval)

oldHour = 60

while True:
    time.sleep(1)
    now = datetime.datetime.now()
    if now.minute == 0:
        if now.hour != oldHour:
            oldHour = now.hour
            playIndex = now.hour % 12
            sound = pygame.mixer.Sound('alarmaudio/start.wav')
            sound.set_volume(audio_volume)
            sound.play()
            time.sleep(audio_interval)

            if (playIndex) == 0:
                sound = pygame.mixer.Sound('alarmaudio/12.wav')
            else:
                sound = pygame.mixer.Sound('alarmaudio/{0}.wav'.format(playIndex))

            sound.set_volume(audio_volume)
            sound.play()
