# Smart Parenting Care Robot
# Raspberry Pi Control Program

import telepot
import RPi.GPIO as GPIO
from time import sleep
import cv2

# Telegram Bot Token
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

bot = telepot.Bot(TOKEN)

# Motor Pins
IN1 = 17
IN2 = 18
IN3 = 22
IN4 = 23

GPIO.setmode(GPIO.BCM)

GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

def move_forward():
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)
    GPIO.output(IN3, True)
    GPIO.output(IN4, False)

def move_backward():
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)
    GPIO.output(IN3, False)
    GPIO.output(IN4, True)

def stop_robot():
    GPIO.output(IN1, False)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)
    GPIO.output(IN4, False)

def capture_image():
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    if ret:
        cv2.imwrite("child_monitor.jpg", frame)
    cam.release()

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    if command == '/start':
        bot.sendMessage(chat_id, "Smart Parenting Care Robot Activated")

    elif command == 'forward':
        move_forward()
        bot.sendMessage(chat_id, "Robot Moving Forward")

    elif command == 'backward':
        move_backward()
        bot.sendMessage(chat_id, "Robot Moving Backward")

    elif command == 'stop':
        stop_robot()
        bot.sendMessage(chat_id, "Robot Stopped")

    elif command == 'camera':
        capture_image()
        bot.sendPhoto(chat_id, photo=open('child_monitor.jpg', 'rb'))

bot.message_loop(handle)

print("Robot Ready...")

while True:
    sleep(10)




import os
import time
import RPi.GPIO as GPIO
import telepot
import pygame
from gtts import gTTS
from mutagen.mp3 import MP3

# ---------------- GPIO SETUP ----------------
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Motor 1 pins
IN1 = 21
IN2 = 20
IN3 = 12
IN4 = 16

GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

GPIO.output(IN1, False)
GPIO.output(IN2, False)
GPIO.output(IN3, False)
GPIO.output(IN4, False)

# Door motor 1 pins
IN5 = 6
IN6 = 5
GPIO.setup(IN5, GPIO.OUT)
GPIO.setup(IN6, GPIO.OUT)
GPIO.output(IN5, False)
GPIO.output(IN6, False)

# Door motor 2 pins
IN7 = 8
IN8 = 7
GPIO.setup(IN7, GPIO.OUT)
GPIO.setup(IN8, GPIO.OUT)
GPIO.output(IN7, False)
GPIO.output(IN8, False)

# Optional third door motor pins
IN9 = 25
IN10 = 24
GPIO.setup(IN9, GPIO.OUT)
GPIO.setup(IN10, GPIO.OUT)
GPIO.output(IN9, False)
GPIO.output(IN10, False)

# ---------------- VOICE FUNCTION ----------------
def play_voice(text1):
    myobj = gTTS(text=text1, lang='en', tld='com', slow=False)
    myobj.save("voice.mp3")
    print("\n------------ Playing --------------\n")

    song = MP3("voice.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("voice.mp3")
    pygame.mixer.music.play()
    time.sleep(song.info.length)
    pygame.quit()

# ---------------- MOVEMENT FUNCTIONS ----------------
def FORWORD():
    print("FORWORD")
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)
    GPIO.output(IN3, False)
    GPIO.output(IN4, True)
    time.sleep(2)

def BACKWORD():
    print("BACKWORD")
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)
    GPIO.output(IN3, True)
    GPIO.output(IN4, False)
    time.sleep(2)

def STOP():
    print("STOP")
    GPIO.output(IN1, False)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)
    GPIO.output(IN4, False)
    time.sleep(1)

def LEFT():
    print("LEFT")
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)
    GPIO.output(IN4, True)
    time.sleep(2)

def RIGHT():
    print("RIGHT")
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)
    GPIO.output(IN3, True)
    GPIO.output(IN4, False)
    time.sleep(2)

# ---------------- DOOR CONTROL ----------------
def Door_one():
    GPIO.output(IN5, False)
    GPIO.output(IN6, True)
    time.sleep(1)

    GPIO.output(IN5, False)
    GPIO.output(IN6, False)
    time.sleep(5)

    GPIO.output(IN5, True)
    GPIO.output(IN6, False)
    time.sleep(1)

    GPIO.output(IN5, False)
    GPIO.output(IN6, False)
    time.sleep(1)

def Door_two():
    GPIO.output(IN7, False)
    GPIO.output(IN8, True)
    time.sleep(1)

    GPIO.output(IN7, False)
    GPIO.output(IN8, False)
    time.sleep(5)

    GPIO.output(IN7, True)
    GPIO.output(IN8, False)
    time.sleep(1)

    GPIO.output(IN7, False)
    GPIO.output(IN8, False)
    time.sleep(1)

def Door_three():
    GPIO.output(IN9, False)
    GPIO.output(IN10, True)
    time.sleep(1)

    GPIO.output(IN9, False)
    GPIO.output(IN10, False)
    time.sleep(5)

    GPIO.output(IN9, True)
    GPIO.output(IN10, False)
    time.sleep(1)

    GPIO.output(IN9, False)
    GPIO.output(IN10, False)
    time.sleep(1)

# ---------------- MOVEMENT PATTERN ----------------
def Move():
    FORWORD()
    STOP()
    LEFT()
    STOP()
    FORWORD()
    STOP()
    RIGHT()
    STOP()
    FORWORD()
    STOP()

# ---------------- MAIN PROGRAM ----------------
try:
    while True:
        FORWORD()
        STOP()
        BACKWORD()
        STOP()
        LEFT()
        STOP()
        RIGHT()
        STOP()

except KeyboardInterrupt:
    print("Program stopped by user")

finally:
    GPIO.cleanup()


#You can also add this explanation in README if needed:
#Controls robot movement using Raspberry Pi GPIO
#Receives commands from Telegram
#Commands like:
#forward
#backward
#stop
#camera
#Captures image using webcam
#Sends photo to caregiver through Telegram
