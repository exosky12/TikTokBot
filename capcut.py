# bot for Pixel 4 on AVD in Android Tiramisu

import os
import time
import subprocess

number_video = len(os.listdir("./video"))
i = 1

print("""
  /$$$$$$  /$$                           /$$$$$$$   /$$$$$$  /$$$$$$$$
 /$$__  $$| $$                          | $$__  $$ /$$__  $$|__  $$__/
| $$  \__/| $$$$$$$   /$$$$$$  /$$   /$$| $$  \ $$| $$  \ $$   | $$
| $$      | $$__  $$ /$$__  $$| $$  | $$| $$$$$$$ | $$  | $$   | $$
| $$      | $$  \ $$| $$  \ $$| $$  | $$| $$__  $$| $$  | $$   | $$
| $$    $$| $$  | $$| $$  | $$| $$  | $$| $$  \ $$| $$  | $$   | $$
|  $$$$$$/| $$  | $$|  $$$$$$/|  $$$$$$/| $$$$$$$/|  $$$$$$/   | $$
 \______/ |__/  |__/ \______/  \______/ |_______/  \______/    |__/

                                                                      """)

print("""List event:
""")

os.system("start emulator -avd CapcutBot_API_33")
time.sleep(80)


while number_video >= i:
    print("Video #" + str(i))
    print("=======")
    os.system("adb reboot")
    time.sleep(65)
    print("[!] rebooted")
    os.system("adb shell pm clear com.google.android.documentsui ")
    os.system("adb shell pm clear com.lemon.lvoverseas ")
    os.system("adb shell rm /storage/emulated/0/DCIM/* ")
    os.system("adb shell rm /storage/emulated/0/DCIM/CapCut/* ")
    os.system("adb shell rm /storage/emulated/0/DCIM/Camera/* ")
    os.system("adb shell pm clear com.lemon.lvoverseas ")
    print("[!] All files and app cleaned")
    os.system("adb push ./video/video" + str(i) +
              ".mp4 /storage/emulated/0/DCIM/ ")
    time.sleep(13)
    print("[!] Video #" + str(i) + " moved")
    os.system(
        "adb shell monkey -p com.google.android.documentsui -c android.intent.category.LAUNCHER 1 ")
    time.sleep(12)
      # menu burger
    os.system("adb shell input tap 111 174")
    time.sleep(3)
      # go storage
    os.system("adb shell input tap 351 1311")
    time.sleep(3)
      # go DCIM
    os.system("adb shell input tap 771 828")
    time.sleep(3)
      # play video to add on gallery
    os.system("adb shell input tap 394 1061")
    time.sleep(3)
      # return home
    os.system("adb shell input keyevent 3")
    os.system("adb shell pm clear com.google.android.documentsui ")
    print("(*) Video imported")
    os.system(
        "adb shell monkey -p com.lemon.lvoverseas -c android.intent.category.LAUNCHER 1 ")
    print("[!] Capcut opened")
    time.sleep(4)
      # accept terms
    os.system("adb shell input tap 409 1570")
    time.sleep(15)
      # accept notifications
    os.system("adb shell input tap 530 1247")
    time.sleep(5)
      # add project
    os.system("adb shell input tap 467 478")
    time.sleep(5)
      # accept access file
    os.system("adb shell input tap 461 1276")
    time.sleep(5)
      # choose video capcut
    os.system("adb shell input tap 212 452")
    time.sleep(10)
      # pause rendu
    os.system("adb shell input tap 551 1088")
    time.sleep(10)
      # continue add
    os.system("adb shell input tap 823 2122")
    time.sleep(10)
      # accept compression
    os.system("adb shell input tap 548 1229")
    print("(*) Capcut video imported")
      # text
    time.sleep(240)
    os.system("adb shell input tap 435 2103")
    time.sleep(13)
    os.system("adb shell input tap 435 2103")
    time.sleep(14)
      # ai subtitles
    os.system("adb shell input tap 551 2099")
    time.sleep(14)
      # selec language
    os.system("adb shell input tap 915 1689")
    time.sleep(15)
      # swipe en -> fr
    os.system("adb shell input touchscreen swipe 484 1796 539 986")
    time.sleep(12)
      # selec fr
    os.system("adb shell input tap 183 1562")
    time.sleep(15)
      # back
    os.system("adb shell input tap 88 1342")
    time.sleep(13)
      # dynamic subtitles
    os.system("adb shell input tap 979 1850")
    time.sleep(13)
      # start ai
    os.system("adb shell input tap 507 2120")
    print("[!] Subtitles added to video#" + str(i))
    time.sleep(91)
      # 720p -> 1080p
    os.system("adb shell input tap 886 73")
    time.sleep(13)
    os.system("adb shell input tap 1037 328")
    time.sleep(13)
      # return back
    os.system("adb shell input tap 525 1195")
    print("(*) Video converted 1080p")
    time.sleep(12)
      # export
    os.system("adb shell input tap 1011 56")
    time.sleep(120)
    print("[!] Video exported")
    os.system("adb shell input keyevent 3")
    time.sleep(2)
      # get name of exported video
    os.system("adb shell ls /storage/emulated/0/DCIM/Camera > data.txt")
    print("---> Verification video...")
    with open('data.txt', 'r') as file:
      data = file.read().replace('\n', '')
    if data == "":
      print("---> Verification failed ! Retrying...")
      # faudrait ajouter commande pour reset et redémarer l'AVD
      os.system("taskkill /f /im qemu-system-x86_64.exe")
      os.system("taskkill /f /im emulator.exe")
      os.system("del data.txt")
      os.system("start emulator -avd CapcutBot_API_33")
      time.sleep(100)
    else:
      print("---> Verification passed !")
      os.system("adb pull /storage/emulated/0/DCIM/Camera/" +
                data + " ./video/video" + str(i) + ".mp4")
      print("[!] Video transfered from Capcut")
      os.system("del data.txt")
      i = i + 1
      data = ""

os.system("taskkill /f /im qemu-system-x86_64.exe")

os.system("python montage.py")
