import pynput
from pynput.mouse import Button
from pynput.keyboard import Key
import time
import os

############################################################################################

os.system("cd")
os.system("start chrome")
time.sleep(5)

############################################################################################

keyboard = pynput.keyboard.Controller()

keyboard.type("https://www.tiktok.com/upload?lang=fr%27")

time.sleep(2)

keyboard.press(Key.enter)
keyboard.release(Key.enter)

time.sleep(6)

mouse = pynput.mouse.Controller()

mouse.position = (0, 0)
time.sleep(3)
mouse.move(900, 360)
time.sleep(2)
mouse.click(Button.left)
time.sleep(4)
keyboard.type("N'hésite pas à t'abonner, il y a de l'exclu qui sort tous les jours ")
time.sleep(2)
keyboard.type("#twitch")
time.sleep(2)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(2)
keyboard.type(" #fyp")
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(2)
keyboard.type(" #foryoupage")
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(2)
keyboard.type(" #stream")
time.sleep(2)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(2)

mouse.position = (0, 0)
time.sleep(2)
mouse.move(600, 370)
time.sleep(1)
mouse.click(Button.left)


mouse.position = (0, 0)
time.sleep(2)
mouse.move(600, 55)
time.sleep(1)
mouse.click(Button.left)

time.sleep(1)

keyboard.type("C:/Users/jules/Desktop/TikTokBot/montage/result")
keyboard.press(Key.enter)
keyboard.release(Key.enter)

mouse.position = (0, 0)
time.sleep(2)
mouse.move(350, 150)
time.sleep(1)
mouse.click(Button.left)

mouse.position = (0, 0)
time.sleep(2)
mouse.move(750, 470)
time.sleep(1)
mouse.click(Button.left)
time.sleep(30)

mouse.position = (0, 0)
time.sleep(2)
mouse.move(1105, 840)
time.sleep(1)
mouse.click(Button.left)


mouse.position = (0, 0)
time.sleep(2)
mouse.move(1050, 1000)
time.sleep(1)
mouse.click(Button.left)
time.sleep(30)

os.system('taskkill /IM chrome.exe')