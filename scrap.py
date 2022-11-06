########################################### IMPORT ##########################################

import requests
from requests.structures import CaseInsensitiveDict
import datetime
import os
from moviepy.editor import *

########################################### KEYS ############################################

headers = CaseInsensitiveDict()
headers["Authorization"] = "Bearer 22xe9dvwvecit9psaezne64420tzlv"
headers["Client-Id"] = "s5v8v6wuj7kw0gbbstinfapqr3sdm7"

########################################### DAYS ############################################

today = datetime.datetime.now(datetime.timezone.utc)
todayRFC3339 = today.isoformat().replace('+00:00', 'Z')
yesterday = today - datetime.timedelta(1)
yesterday7RFC3339 = yesterday.isoformat().replace('+00:00', 'Z')

########################################### Find ID ##########################################

# urlID = "https://api.twitch.tv/helix/users?login=streamerName"
# respo = requests.get(urlID, headers=headers)
# print(respo.text)

############################################ IDS #############################################

gotagaID = "24147592"
antoineDanielID = "135468063"
jbzzedID = "114497555"
kametoID = "27115917"
lebouseuhID = "96562014"
valouzID = "39129104"
domingoID = "40063341"
squeezieID = "52130765"
ponceID = "50597026"
billyID = "407837457"
amineID = "407388596"
melchiorID = "85977125"
lincaID = "144395004"
locklearID = "137347549"
luttiID = "89047775"
papesanID = "485818115"
wankilstudioID = "31289086"
mickalowID = "30709418"
ultiaID = "68594999"
sardID = "50795214"

############################################ GAMES IDS ######################################

games = {
    "515025": "overwatch",
    "33214": "fortnite",
    "30921": "rocket league",
    "509658": "discute",
    "511224": "apex legends",
    "27471": "minecraft",
    "510218": "among us",
    "514858": "league of legends",
    "516575": "valorant",
    "3235": "gta",
    "29595": "dota",
    "18122": "world of warcraft",
    "32399": "csgo",
    "513181": "genshin impact",
    "417752": "discute",
    "582372781": "decouvre",
    "11103": "uno",
    "896525007": "gas station",
    "458641": "uncharted",
    "1678052513": "MW2",
    "519103": "PowerWash",
    "509663": "event",
    "21779": "League of Legends",
    "512953": "Elden Ring",
    "1407310739": "Borderlands",
    "513891": "Darq",
    "1833197007": "Tower Of Fantasy",
    "1228709591": "Plague Tale",
    "518144": "Outlast Trials",
    "1311006114": "Father's Day",
    "32982": "GTA",
    "494082": "Visage",
    "493057": "PUBG",
    "488190": "Poker",
    "491168": "Clash Royal",
}

dir = './video'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))
dir2 = './videoTitles'
for f in os.listdir(dir2):
    os.remove(os.path.join(dir2, f))
dir3 = './result'
for f in os.listdir(dir3):
    os.remove(os.path.join(dir3, f))
dir4 = './tmp'
for f in os.listdir(dir4):
    os.remove(os.path.join(dir4, f))
dir5 = './final'
for f in os.listdir(dir5):
    os.remove(os.path.join(dir5, f))

############################################ GENERAL ########################################

index = 0
duration = 0

############################################ Gotaga #########################################

gotagaClip = "https://api.twitch.tv/helix/clips?broadcaster_id=" + gotagaID + "&started_at=" + \
    yesterday7RFC3339 + "&ended_at=" + todayRFC3339 + "&first=1"
gotagaRequest = requests.get(gotagaClip, headers=headers)
gotagaResponse = gotagaRequest.json()
gotagaResult = gotagaResponse.get('data')
for element in gotagaResult:
    url = element.get('url')
    gameID = element.get('game_id')
    if url == "":
        index = index
    else:
        index = index + 1
        ClipDl = os.system(
            "twitch-dl download -q source --overwrite --output ./video/video" + str(index) + ".mp4 " + url)
        f = open("./videoTitles/video" + str(index) + ".txt", "w+")
        if gameID in games:
            if gameID == "417752" or gameID == "509658":
                f.write("Gotaga discute avec les viewers et dit des dingueries")
            elif gameID == "509663":
                f.write("Gotaga fais des dingueries durant l'event")
            else:
                f.write("Gotaga fait des dingueries sur " + games[gameID])
        else:
            f.write("Gotaga fou le zbeul")
        f.close()
        clip = VideoFileClip("video/video"+str(index)+".mp4")
        duration = duration + int(clip.duration)
        if duration >= 62:
            os.system("python capcut.py")
            duration = 0
            index = 0
            number_video = len(os.listdir("./video"))
            for i in range(number_video):
                os.system("del /s /q /f video" + str(i+1) + ".mp4")
                os.system("del /s /q /f video" + str(i+1) + ".txt")

########################################## Antoine Daniel ##################################

antoineClip = "https://api.twitch.tv/helix/clips?broadcaster_id=" + antoineDanielID + "&started_at=" + \
    yesterday7RFC3339 + "&ended_at=" + todayRFC3339 + "&first=1"
antoineRequest = requests.get(antoineClip, headers=headers)
antoineResponse = antoineRequest.json()
antoineResult = antoineResponse.get('data')
for element in antoineResult:
    url = element.get('url')
    gameID = element.get('game_id')
    if url == "":
        index = index
    elif gameID == "509663":
        f.write("Antoine fais des dingueries durant l'event")
    else:
        index = index + 1
        ClipDl = os.system(
            "twitch-dl download -q source --overwrite --output ./video/video" + str(index) + ".mp4 " + url)
        f = open("./videoTitles/video" + str(index) + ".txt", "w+")
        if gameID in games:
            if gameID == "417752" or gameID == "509658":
                f.write("Antoine discute avec les viewers et dit des dingueries")
            elif gameID == "509663":
                f.write("Antoine fais des dingueries durant l'event")
            else:
                f.write("Antoine fait des dingueries sur " + games[gameID])
        else:
            f.write("Antoine fou le zbeul")
        f.close()
        clip = VideoFileClip("video/video"+str(index)+".mp4")
        duration = duration + int(clip.duration)
        if duration >= 62:
            os.system("python capcut.py")
            duration = 0
            index = 0
            number_video = len(os.listdir("./video"))
            for i in range(number_video):
                os.system("del /s /q video" + str(i+1) + ".mp4")
                os.system("del /s /q video" + str(i+1) + ".txt")

########################################### Jbzzed ##########################################

jbzzedClip = "https://api.twitch.tv/helix/clips?broadcaster_id=" + jbzzedID + "&started_at=" + \
    yesterday7RFC3339 + "&ended_at=" + todayRFC3339 + "&first=1"
jbzzedRequest = requests.get(jbzzedClip, headers=headers)
jbzzedResponse = jbzzedRequest.json()
jbzzedResult = jbzzedResponse.get('data')
for element in jbzzedResult:
    url = element.get('url')
    gameID = element.get('game_id')
    if url == "":
        index = index
    elif gameID == "509663":
        f.write("Jbzzed fais des dingueries durant l'event")
    else:
        index = index + 1
        ClipDl = os.system(
            "twitch-dl download -q source --overwrite --output ./video/video" + str(index) + ".mp4 " + url)
        f = open("./videoTitles/video" + str(index) + ".txt", "w+")
        if gameID in games:
            if gameID == "417752" or gameID == "509658":
                f.write("Jbzzed discute avec les viewers et dit des dingueries")
            elif gameID == "509663":
                f.write("Jbzzed fais des dingueries durant l'event")
            else:
                f.write("Jbzzed fait des dingueries sur " + games[gameID])
        else:
            f.write("Jbzzed fou le zbeul")
        f.close()
        clip = VideoFileClip("video/video"+str(index)+".mp4")
        duration = duration + int(clip.duration)
        if duration >= 62:
            os.system("python capcut.py")
            duration = 0
            index = 0
            number_video = len(os.listdir("./video"))
            for i in range(number_video):
                os.system("del /s /q video" + str(i+1) + ".mp4")
                os.system("del /s /q video" + str(i+1) + ".txt")

########################################### Kameto ##########################################

kametoClip = "https://api.twitch.tv/helix/clips?broadcaster_id=" + kametoID + "&started_at=" + \
    yesterday7RFC3339 + "&ended_at=" + todayRFC3339 + "&first=1"
kametoRequest = requests.get(kametoClip, headers=headers)
kametoResponse = kametoRequest.json()
kametoResult = kametoResponse.get('data')
for element in kametoResult:
    url = element.get('url')
    gameID = element.get('game_id')
    if url == "":
        index = index
    elif gameID == "509663":
        f.write("Kameto fais des dingueries durant l'event")
    else:
        index = index + 1
        ClipDl = os.system(
            "twitch-dl download -q source --overwrite --output ./video/video" + str(index) + ".mp4 " + url)
        f = open("./videoTitles/video" + str(index) + ".txt", "w+")
        if gameID in games:
            if gameID == "417752" or gameID == "509658":
                f.write("Kameto discute avec les viewers et dit des dingueries")
            elif gameID == "509663":
                f.write("Kameto fais des dingueries durant l'event")
            else:
                f.write("Kameto fait des dingueries sur " + games[gameID])
        else:
            f.write("Kameto fou le zbeul")
        f.close()
        clip = VideoFileClip("video/video"+str(index)+".mp4")
        duration = duration + int(clip.duration)
        if duration >= 62:
            os.system("python capcut.py")
            duration = 0
            index = 0
            number_video = len(os.listdir("./video"))
            for i in range(number_video):
                os.system("del /s /q video" + str(i+1) + ".mp4")
                os.system("del /s /q video" + str(i+1) + ".txt")
                
########################################### Lebouseuh #######################################

lebouseuhClip = "https://api.twitch.tv/helix/clips?broadcaster_id=" + lebouseuhID + "&started_at=" + \
    yesterday7RFC3339 + "&ended_at=" + todayRFC3339 + "&first=1"
lebouseuhRequest = requests.get(lebouseuhClip, headers=headers)
lebouseuhResponse = lebouseuhRequest.json()
lebouseuhResult = lebouseuhResponse.get('data')
for element in lebouseuhResult:
    url = element.get('url')
    gameID = element.get('game_id')
    if url == "":
        index = index
    elif gameID == "509663":
        f.write("Lebouseuh fais des dingueries durant l'event")
    else:
        index = index + 1
        ClipDl = os.system(
            "twitch-dl download -q source --overwrite --output ./video/video" + str(index) + ".mp4 " + url)
        f = open("./videoTitles/video" + str(index) + ".txt", "w+")
        if gameID in games:
            if gameID == "417752" or gameID == "509658":
                f.write("Lebouseuh discute avec les viewers et dit des dingueries")
            elif gameID == "509663":
                f.write("Lebouseuh fais des dingueries durant l'event")
            else:
                f.write("Lebouseuh fait des dingueries sur " + games[gameID])
        else:
            f.write("Lebouseuh fou le zbeul")
        f.close()
        clip = VideoFileClip("video/video"+str(index)+".mp4")
        duration = duration + int(clip.duration)
        if duration >= 62:
            os.system("python capcut.py")
            duration = 0
            index = 0
            number_video = len(os.listdir("./video"))
            for i in range(number_video):
                os.system("del /s /q video" + str(i+1) + ".mp4")
                os.system("del /s /q video" + str(i+1) + ".txt")

########################################### Valouz ##########################################

valouzClip = "https://api.twitch.tv/helix/clips?broadcaster_id=" + valouzID + "&started_at=" + \
    yesterday7RFC3339 + "&ended_at=" + todayRFC3339 + "&first=1"
valouzRequest = requests.get(valouzClip, headers=headers)
valouzResponse = valouzRequest.json()
valouzResult = valouzResponse.get('data')
for element in valouzResult:
    url = element.get('url')
    gameID = element.get('game_id')
    if url == "":
        index = index
    elif gameID == "509663":
        f.write("Valouz fais des dingueries durant l'event")
    else:
        index = index + 1
        ClipDl = os.system(
            "twitch-dl download -q source --overwrite --output ./video/video" + str(index) + ".mp4 " + url)
        f = open("./videoTitles/video" + str(index) + ".txt", "w+")
        if gameID in games:
            if gameID == "417752" or gameID == "509658":
                f.write("Valouz discute avec les viewers et dit des dingueries")
            elif gameID == "509663":
                f.write("Valouz fais des dingueries durant l'event")
            else:
                f.write("Valouz fait des dingueries sur " + games[gameID])
        else:
            f.write("Valouz fou le zbeul")
        f.close()
        clip = VideoFileClip("video/video"+str(index)+".mp4")
        duration = duration + int(clip.duration)
        if duration >= 62:
            os.system("python capcut.py")
            duration = 0
            index = 0
            number_video = len(os.listdir("./video"))
            for i in range(number_video):
                os.system("del /s /q video" + str(i+1) + ".mp4")
                os.system("del /s /q video" + str(i+1) + ".txt")

########################################### Domingo #########################################

domingoClip = "https://api.twitch.tv/helix/clips?broadcaster_id=" + domingoID + "&started_at=" + \
    yesterday7RFC3339 + "&ended_at=" + todayRFC3339 + "&first=1"
domingoRequest = requests.get(domingoClip, headers=headers)
domingoResponse = domingoRequest.json()
domingoResult = domingoResponse.get('data')
for element in domingoResult:
    url = element.get('url')
    gameID = element.get('game_id')
    if url == "":
        index = index
    elif gameID == "509663":
        f.write("Domingo fais des dingueries durant l'event")
    else:
        index = index + 1
        ClipDl = os.system(
            "twitch-dl download -q source --overwrite --output ./video/video" + str(index) + ".mp4 " + url)
        f = open("./videoTitles/video" + str(index) + ".txt", "w+")
        if gameID in games:
            if gameID == "417752" or gameID == "509658":
                f.write("Domingo discute avec les viewers et dit des dingueries")
            elif gameID == "509663":
                f.write("Domingo fais des dingueries durant l'event")
            else:
                f.write("Domingo fait des dingueries sur " + games[gameID])
        else:
            f.write("Domingo fou le zbeul")
        f.close()
        clip = VideoFileClip("video/video"+str(index)+".mp4")
        duration = duration + int(clip.duration)
        if duration >= 62:
            os.system("python capcut.py")
            duration = 0
            index = 0
            number_video = len(os.listdir("./video"))
            for i in range(number_video):
                os.system("del /s /q video" + str(i+1) + ".mp4")
                os.system("del /s /q video" + str(i+1) + ".txt")

########################################### Squeezie ########################################

squeezieClip = "https://api.twitch.tv/helix/clips?broadcaster_id=" + squeezieID + "&started_at=" + \
    yesterday7RFC3339 + "&ended_at=" + todayRFC3339 + "&first=1"
squeezieRequest = requests.get(squeezieClip, headers=headers)
squeezieResponse = squeezieRequest.json()
squeezieResult = squeezieResponse.get('data')
for element in squeezieResult:
    url = element.get('url')
    gameID = element.get('game_id')
    if url == "":
        index = index
    elif gameID == "509663":
        f.write("Squeezie fais des dingueries durant l'event")
    else:
        index = index + 1
        ClipDl = os.system(
            "twitch-dl download -q source --overwrite --output ./video/video" + str(index) + ".mp4 " + url)
        f = open("./videoTitles/video" + str(index) + ".txt", "w+")
        if gameID in games:
            if gameID == "417752" or gameID == "509658":
                f.write("Squeezie discute avec les viewers et dit des dingueries")
            elif gameID == "509663":
                f.write("Squeezie fais des dingueries durant l'event")
            else:
                f.write("Squeezie fait des dingueries sur " + games[gameID])
        else:
            f.write("Squeezie fou le zbeul")
        f.close()
        clip = VideoFileClip("video/video"+str(index)+".mp4")
        duration = duration + int(clip.duration)
        if duration >= 62:
            os.system("python capcut.py")
            duration = 0
            index = 0
            number_video = len(os.listdir("./video"))
            for i in range(number_video):
                os.system("del /s /q video" + str(i+1) + ".mp4")
                os.system("del /s /q video" + str(i+1) + ".txt")

########################################### Ponce ###########################################

ponceClip = "https://api.twitch.tv/helix/clips?broadcaster_id=" + ponceID + "&started_at=" + \
    yesterday7RFC3339 + "&ended_at=" + todayRFC3339 + "&first=1"
ponceRequest = requests.get(ponceClip, headers=headers)
ponceResponse = ponceRequest.json()
ponceResult = ponceResponse.get('data')
for element in ponceResult:
    url = element.get('url')
    gameID = element.get('game_id')
    if url == "":
        index = index
    elif gameID == "509663":
        f.write("Ponce fais des dingueries durant l'event")
    else:
        index = index + 1
        ClipDl = os.system(
            "twitch-dl download -q source --overwrite --output ./video/video" + str(index) + ".mp4 " + url)
        f = open("./videoTitles/video" + str(index) + ".txt", "w+")
        if gameID in games:
            if gameID == "417752" or gameID == "509658":
                f.write("Ponce discute avec les viewers et dit des dingueries")
            elif gameID == "509663":
                f.write("Ponce fais des dingueries durant l'event")
            else:
                f.write("Ponce fait des dingueries sur " + games[gameID])
        else:
            f.write("Ponce fou le zbeul")
        f.close()
        clip = VideoFileClip("video/video"+str(index)+".mp4")
        duration = duration + int(clip.duration)
        if duration >= 62:
            os.system("python capcut.py")
            duration = 0
            index = 0
            number_video = len(os.listdir("./video"))
            for i in range(number_video):
                os.system("del /s /q video" + str(i+1) + ".mp4")
                os.system("del /s /q video" + str(i+1) + ".txt")

########################################## Billy ###########################################

billyClip = "https://api.twitch.tv/helix/clips?broadcaster_id=" + billyID + "&started_at=" + \
    yesterday7RFC3339 + "&ended_at=" + todayRFC3339 + "&first=1"
billyRequest = requests.get(billyClip, headers=headers)
billyResponse = billyRequest.json()
billyResult = billyResponse.get('data')
for element in billyResult:
    url = element.get('url')
    gameID = element.get('game_id')
    if url == "":
        index = index
    elif gameID == "509663":
        f.write("Billy fais des dingueries durant l'event")
    else:
        index = index + 1
        ClipDl = os.system(
            "twitch-dl download -q source --overwrite --output ./video/video" + str(index) + ".mp4 " + url)
        f = open("./videoTitles/video" + str(index) + ".txt", "w+")
        if gameID in games:
            if gameID == "417752" or gameID == "509658":
                f.write("Billy discute avec les viewers et dit des dingueries")
            elif gameID == "509663":
                f.write("Billy fais des dingueries durant l'event")
            else:
                f.write("Billy fait des dingueries sur " + games[gameID])
        else:
            f.write("Billy fou le zbeul")
        f.close()
        clip = VideoFileClip("video/video"+str(index)+".mp4")
        duration = duration + int(clip.duration)
        if duration >= 62:
            os.system("python capcut.py")
            duration = 0
            index = 0
            number_video = len(os.listdir("./video"))
            for i in range(number_video):
                os.system("del /s /q video" + str(i+1) + ".mp4")
                os.system("del /s /q video" + str(i+1) + ".txt")

########################################### Amine ###########################################

amineClip = "https://api.twitch.tv/helix/clips?broadcaster_id=" + amineID + "&started_at=" + \
    yesterday7RFC3339 + "&ended_at=" + todayRFC3339 + "&first=1"
amineRequest = requests.get(amineClip, headers=headers)
amineResponse = amineRequest.json()
amineResult = amineResponse.get('data')
for element in amineResult:
    url = element.get('url')
    gameID = element.get('game_id')
    if url == "":
        index = index
    elif gameID == "509663":
        f.write("Amine fais des dingueries durant l'event")
    else:
        index = index + 1
        ClipDl = os.system(
            "twitch-dl download -q source --overwrite --output ./video/video" + str(index) + ".mp4 " + url)
        f = open("./videoTitles/video" + str(index) + ".txt", "w+")
        if gameID in games:
            if gameID == "417752" or gameID == "509658":
                f.write("Amine discute avec les viewers et dit des dingueries")
            elif gameID == "509663":
                f.write("Amine fais des dingueries durant l'event")
            else:
                f.write("Amine fait des dingueries sur " + games[gameID])
        else:
            f.write("Amine fou le zbeul")
        f.close()
        clip = VideoFileClip("video/video"+str(index)+".mp4")
        duration = duration + int(clip.duration)
        if duration >= 62:
            os.system("python capcut.py")
            duration = 0
            index = 0
            number_video = len(os.listdir("./video"))
            for i in range(number_video):
                os.system("del /s /q video" + str(i+1) + ".mp4")
                os.system("del /s /q video" + str(i+1) + ".txt")
                

########################################### Melchior ########################################

melchiorClip = "https://api.twitch.tv/helix/clips?broadcaster_id=" + melchiorID + "&started_at=" + \
    yesterday7RFC3339 + "&ended_at=" + todayRFC3339 + "&first=1"
melchiorRequest = requests.get(melchiorClip, headers=headers)
melchiorResponse = melchiorRequest.json()
melchiorResult = melchiorResponse.get('data')
for element in melchiorResult:
    url = element.get('url')
    gameID = element.get('game_id')
    if url == "":
        index = index
    elif gameID == "509663":
        f.write("Melchior fais des dingueries durant l'event")
    else:
        index = index + 1
        ClipDl = os.system(
            "twitch-dl download -q source --overwrite --output ./video/video" + str(index) + ".mp4 " + url)
        f = open("./videoTitles/video" + str(index) + ".txt", "w+")
        if gameID in games:
            if gameID == "417752" or gameID == "509658":
                f.write("Melchior discute avec les viewers et dit des dingueries")
            elif gameID == "509663":
                f.write("Melchior fais des dingueries durant l'event")
            else:
                f.write("Melchior fait des dingueries sur " + games[gameID])
        else:
            f.write("Melchior fou le zbeul")
        f.close()
        clip = VideoFileClip("video/video"+str(index)+".mp4")
        duration = duration + int(clip.duration)
        if duration >= 62:
            os.system("python capcut.py")
            duration = 0
            index = 0
            number_video = len(os.listdir("./video"))
            for i in range(number_video):
                os.system("del /s /q video" + str(i+1) + ".mp4")
                os.system("del /s /q video" + str(i+1) + ".txt")

########################################### Linca ###########################################

lincaClip = "https://api.twitch.tv/helix/clips?broadcaster_id=" + lincaID + "&started_at=" + \
    yesterday7RFC3339 + "&ended_at=" + todayRFC3339 + "&first=1"
lincaRequest = requests.get(lincaClip, headers=headers)
lincaResponse = lincaRequest.json()
lincaResult = lincaResponse.get('data')
for element in lincaResult:
    url = element.get('url')
    gameID = element.get('game_id')
    if url == "":
        index = index
    elif gameID == "509663":
        f.write("Linca fais des dingueries durant l'event")
    else:
        index = index + 1
        ClipDl = os.system(
            "twitch-dl download -q source --overwrite --output ./video/video" + str(index) + ".mp4 " + url)
        f = open("./videoTitles/video" + str(index) + ".txt", "w+")
        if gameID in games:
            if gameID == "417752" or gameID == "509658":
                f.write("Linca discute avec les viewers et dit des dingueries")
            elif gameID == "509663":
                f.write("Linca fais des dingueries durant l'event")
            else:
                f.write("Linca fait des dingueries sur " + games[gameID])
        else:
            f.write("Linca fou le zbeul")
        f.close()
        clip = VideoFileClip("video/video"+str(index)+".mp4")
        duration = duration + int(clip.duration)
        if duration >= 62:
            os.system("python capcut.py")
            duration = 0
            index = 0
            number_video = len(os.listdir("./video"))
            for i in range(number_video):
                os.system("del /s /q video" + str(i+1) + ".mp4")
                os.system("del /s /q video" + str(i+1) + ".txt")

########################################### Locklear ########################################

locklearClip = "https://api.twitch.tv/helix/clips?broadcaster_id=" + locklearID + "&started_at=" + \
    yesterday7RFC3339 + "&ended_at=" + todayRFC3339 + "&first=1"
locklearRequest = requests.get(locklearClip, headers=headers)
locklearResponse = locklearRequest.json()
locklearResult = locklearResponse.get('data')
for element in locklearResult:
    url = element.get('url')
    gameID = element.get('game_id')
    if url == "":
        index = index
    else:
        index = index + 1
        ClipDl = os.system(
            "twitch-dl download -q source --overwrite --output ./video/video" + str(index) + ".mp4 " + url)
        f = open("./videoTitles/video" + str(index) + ".txt", "w+")
        if gameID in games:
            if gameID == "417752" or gameID == "509658":
                f.write("Locklear discute avec les viewers et dit des dingueries")
            elif gameID == "509663":
                f.write("Locklear fais des dingueries durant l'event")
            else:
                f.write("Locklear fait des dingueries sur " + games[gameID])
        else:
            f.write("Locklear fou le zbeul")
        f.close()
        clip = VideoFileClip("video/video"+str(index)+".mp4")
        duration = duration + int(clip.duration)
        if duration >= 62:
            os.system("python capcut.py")
            duration = 0
            index = 0
            number_video = len(os.listdir("./video"))
            for i in range(number_video):
                os.system("del /s /q video" + str(i+1) + ".mp4")
                os.system("del /s /q video" + str(i+1) + ".txt")

########################################### Lutti ###########################################

luttiClip = "https://api.twitch.tv/helix/clips?broadcaster_id=" + luttiID + "&started_at=" + \
    yesterday7RFC3339 + "&ended_at=" + todayRFC3339 + "&first=1"
luttiRequest = requests.get(luttiClip, headers=headers)
luttiResponse = luttiRequest.json()
luttiResult = luttiResponse.get('data')
for element in luttiResult:
    url = element.get('url')
    gameID = element.get('game_id')
    if url == "":
        index = index
    else:
        index = index + 1
        ClipDl = os.system(
            "twitch-dl download -q source --overwrite --output ./video/video" + str(index) + ".mp4 " + url)
        f = open("./videoTitles/video" + str(index) + ".txt", "w+")
        if gameID in games:
            if gameID == "417752" or gameID == "509658":
                f.write("Lutti discute avec les viewers et dit des dingueries")
            elif gameID == "509663":
                f.write("Lutti fais des dingueries durant l'event")
            else:
                f.write("Lutti fait des dingueries sur " + games[gameID])
        else:
            f.write("Lutti fou le zbeul")
        f.close()
        clip = VideoFileClip("video/video"+str(index)+".mp4")
        duration = duration + int(clip.duration)
        if duration >= 62:
            os.system("python capcut.py")
            duration = 0
            index = 0
            number_video = len(os.listdir("./video"))
            for i in range(number_video):
                os.system("del /s /q video" + str(i+1) + ".mp4")
                os.system("del /s /q video" + str(i+1) + ".txt")

########################################### Papesan #########################################

papesanClip = "https://api.twitch.tv/helix/clips?broadcaster_id=" + papesanID + "&started_at=" + \
    yesterday7RFC3339 + "&ended_at=" + todayRFC3339 + "&first=1"
papesanRequest = requests.get(papesanClip, headers=headers)
papesanResponse = papesanRequest.json()
papesanResult = papesanResponse.get('data')
for element in papesanResult:
    url = element.get('url')
    gameID = element.get('game_id')
    if url == "":
        index = index
    else:
        index = index + 1
        ClipDl = os.system(
            "twitch-dl download -q source --overwrite --output ./video/video" + str(index) + ".mp4 " + url)
        f = open("./videoTitles/video" + str(index) + ".txt", "w+")
        if gameID in games:
            if gameID == "417752" or gameID == "509658":
                f.write("Papesan discute avec les viewers et dit des dingueries")
            elif gameID == "509663":
                f.write("Papesan fais des dingueries durant l'event")
            else:
                f.write("Papesan fait des dingueries sur " + games[gameID])
        else:
            f.write("Papesan fou le zbeul")
        f.close()
        clip = VideoFileClip("video/video"+str(index)+".mp4")
        duration = duration + int(clip.duration)
        if duration >= 62:
            os.system("python capcut.py")
            duration = 0
            index = 0
            number_video = len(os.listdir("./video"))
            for i in range(number_video):
                os.system("del /s /q video" + str(i+1) + ".mp4")
                os.system("del /s /q video" + str(i+1) + ".txt")

########################################### Wankilstudio ####################################

wankilstudioClip = "https://api.twitch.tv/helix/clips?broadcaster_id=" + wankilstudioID + "&started_at=" + \
    yesterday7RFC3339 + "&ended_at=" + todayRFC3339 + "&first=1"
wankilstudioRequest = requests.get(wankilstudioClip, headers=headers)
wankilstudioResponse = wankilstudioRequest.json()
wankilstudioResult = wankilstudioResponse.get('data')
for element in wankilstudioResult:
    url = element.get('url')
    gameID = element.get('game_id')
    if url == "":
        index = index
    else:
        index = index + 1
        ClipDl = os.system(
            "twitch-dl download -q source --overwrite --output ./video/video" + str(index) + ".mp4 " + url)
        f = open("./videoTitles/video" + str(index) + ".txt", "w+")
        if gameID in games:
            if gameID == "417752" or gameID == "509658":
                f.write("Wankil discute avec les viewers et dit des dingueries")
            elif gameID == "509663":
                f.write("Wankil fais des dingueries durant l'event")
            else:
                f.write("Wankil fait des dingueries sur " + games[gameID])
        else:
            f.write("Wankil fou le zbeul")
        f.close()
        clip = VideoFileClip("video/video"+str(index)+".mp4")
        duration = duration + int(clip.duration)
        if duration >= 62:
            os.system("python capcut.py")
            duration = 0
            index = 0
            number_video = len(os.listdir("./video"))
            for i in range(number_video):
                os.system("del /s /q video" + str(i+1) + ".mp4")
                os.system("del /s /q video" + str(i+1) + ".txt")

########################################### Mickalow ########################################

mickalowClip = "https://api.twitch.tv/helix/clips?broadcaster_id=" + mickalowID + "&started_at=" + \
    yesterday7RFC3339 + "&ended_at=" + todayRFC3339 + "&first=1"
mickalowRequest = requests.get(mickalowClip, headers=headers)
mickalowResponse = mickalowRequest.json()
mickalowResult = mickalowResponse.get('data')
for element in mickalowResult:
    url = element.get('url')
    gameID = element.get('game_id')
    if url == "":
        index = index
    else:
        index = index + 1
        ClipDl = os.system(
            "twitch-dl download -q source --overwrite --output ./video/video" + str(index) + ".mp4 " + url)
        f = open("./videoTitles/video" + str(index) + ".txt", "w+")
        if gameID in games:
            if gameID == "417752" or gameID == "509658":
                f.write("Mickalow discute avec les viewers et dit des dingueries")
            elif gameID == "509663":
                f.write("Mickalow fais des dingueries durant l'event")
            else:
                f.write("Mickalow fait des dingueries sur " + games[gameID])
        else:
            f.write("Mickalow fou le zbeul")
        f.close()
        clip = VideoFileClip("video/video"+str(index)+".mp4")
        duration = duration + int(clip.duration)
        if duration >= 62:
            os.system("python capcut.py")
            duration = 0
            index = 0
            number_video = len(os.listdir("./video"))
            for i in range(number_video):
                os.system("del /s /q video" + str(i+1) + ".mp4")
                os.system("del /s /q video" + str(i+1) + ".txt")

########################################### Ultia ###########################################

ultiaClip = "https://api.twitch.tv/helix/clips?broadcaster_id=" + ultiaID + "&started_at=" + \
    yesterday7RFC3339 + "&ended_at=" + todayRFC3339 + "&first=1"
ultiaRequest = requests.get(ultiaClip, headers=headers)
ultiaResponse = ultiaRequest.json()
ultiaResult = ultiaResponse.get('data')
for element in ultiaResult:
    url = element.get('url')
    gameID = element.get('game_id')
    if url == "":
        index = index
    else:
        index = index + 1
        ClipDl = os.system(
            "twitch-dl download -q source --overwrite --output ./video/video" + str(index) + ".mp4 " + url)
        f = open("./videoTitles/video" + str(index) + ".txt", "w+")
        if gameID in games:
            if gameID == "417752" or gameID == "509658":
                f.write("Ultia discute avec les viewers et dit des dingueries")
            elif gameID == "509663":
                f.write("Ultia fais des dingueries durant l'event")
            else:
                f.write("Ultia fait des dingueries sur " + games[gameID])
        else:
            f.write("Ultia fou le zbeul")
        f.close()
        clip = VideoFileClip("video/video"+str(index)+".mp4")
        duration = duration + int(clip.duration)
        if duration >= 62:
            os.system("python capcut.py")
            duration = 0
            index = 0
            number_video = len(os.listdir("./video"))
            for i in range(number_video):
                os.system("del /s /q video" + str(i+1) + ".mp4")
                os.system("del /s /q video" + str(i+1) + ".txt")

########################################### Sardoche ########################################

sardClip = "https://api.twitch.tv/helix/clips?broadcaster_id=" + sardID + "&started_at=" + \
    yesterday7RFC3339 + "&ended_at=" + todayRFC3339 + "&first=1"
sardRequest = requests.get(sardClip, headers=headers)
sardResponse = sardRequest.json()
sardResult = sardResponse.get('data')
for element in sardResult:
    url = element.get('url')
    gameID = element.get('game_id')
    if url == "":
        index = index
    else:
        index = index + 1
        ClipDl = os.system(
            "twitch-dl download -q source --overwrite --output ./video/video" + str(index) + ".mp4 " + url)
        f = open("./videoTitles/video" + str(index) + ".txt", "w+")
        if gameID in games:
            if gameID == "417752" or gameID == "509658":
                f.write("Sardoche discute avec les viewers et dit des dingueries")
            elif gameID == "509663":
                f.write("Sardoche fais des dingueries durant l'event")
            else:
                f.write("Sardoche fait des dingueries sur " + games[gameID])
        else:
            f.write("Sardoche fou le zbeul")
        f.close()
        clip = VideoFileClip("video/video"+str(index)+".mp4")
        duration = duration + int(clip.duration)
        if duration >= 62:
            os.system("python capcut.py")
            duration = 0
            index = 0
            number_video = len(os.listdir("./video"))
            for i in range(number_video):
                os.system("del /s /q video" + str(i+1) + ".mp4")
                os.system("del /s /q video" + str(i+1) + ".txt")
