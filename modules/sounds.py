import pygame
import random
import time
pygame.init()
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
class Sounds:
    def __init__ (self):
        self.play_sound = True
    # returns false so the sound will stop
    def stop_sound(self):
        self.play_sound = False
        return self.play_sound
    # returns true so the sound will start
    def start_sound(self):
        return self.play_sound
    # play explosion
    def play_explosion(self):
        explosion_sound = pygame.mixer.Sound("assets/sounds/explosion_1.wav")
        pygame.mixer.Sound.play(explosion_sound)
    # play placing ship sound
    def place_ship(self):
        place_sounds = ["assets/sounds/place_ship_0.wav","assets/sounds/place_ship_1.wav"]
        placing_sound = pygame.mixer.Sound(random.choice(place_sounds))
        pygame.mixer.Sound.play(placing_sound)
    # play exit sound
    def exit_sound(self):
        exit_sfx = pygame.mixer.Sound("assets/sounds/exit_sound.wav")
        pygame.mixer.Sound.play(exit_sfx)
    # play click sound
    def click_sound(self):
        click_sfx = pygame.mixer.Sound("assets/sounds/click_sound.wav")
        pygame.mixer.Sound.play(click_sfx)
    # play error sounds
    def error(self):
        error_sfx = pygame.mixer.Sound("assets/sounds/error.wav")
        pygame.mixer.Sound.play(error_sfx)
    # plays moving sound
    def waves(self):
        waves = pygame.mixer.Sound("assets/sounds/waves.wav")
        pygame.mixer.Sound.play(waves)
    # plays biem sound
    def biem(self):
        biem = pygame.mixer.Sound("assets/sounds/explosion_1.wav")
        pygame.mixer.Sound.play(biem)