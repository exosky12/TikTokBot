########################################### IMPORT ##########################################

import requests
from requests.structures import CaseInsensitiveDict
import datetime
import os
import shutil
from moviepy.editor import *

########################################### CLEAR FILES #####################################

dir = './preVideo'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))

dir2 = './video'
for f in os.listdir(dir2):
    os.remove(os.path.join(dir, f))

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
krlID = "129289579"
melchiorID = "85977125"
lincaID = "144395004"
maghlaID = "131215608"
locklearID = "137347549"
luttiID = "89047775"
papesanID = "485818115"
wankilstudioID = "31289086"
mickalowID = "30709418"
jeelID = "114119743"
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
    "493057": "PUBG"
}

############################################ GENERAL ########################################

index = 0

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
            "twitch-dl download -q source --output ./preVideo/video" + str(index) + ".mp4 " + url)
        f = open("./preVideo/video" + str(index) + ".txt", "w+")
        if gameID == "417752" or gameID == "509658":
            f.write("gotaga discute avec les viewers et dit des dingueries")
        else:
            f.write("gotaga fait des dingueries sur " + games[gameID])
        f.close()

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
    else:
        index = index + 1
        ClipDl = os.system(
            "twitch-dl download -q source --output ./preVideo/video" + str(index) + ".mp4 " + url)
        f = open("./preVideo/video" + str(index) + ".txt", "w+")
        if gameID == "417752" or gameID == "509658":
            f.write("antoine discute avec les viewers et dit des dingueries")
        else:
            f.write("antoine fait des dingueries sur " + games[gameID])
        f.close()

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
    else:
        index = index + 1
        ClipDl = os.system(
            "twitch-dl download -q source --output ./preVideo/video" + str(index) + ".mp4 " + url)
        f = open("./preVideo/video" + str(index) + ".txt", "w+")
        if gameID == "417752" or gameID == "509658":
            f.write("jbzzed discute avec les viewers et dit des dingueries")
        else:
            f.write("jbzzed fait des dingueries sur " + games[gameID])
        f.close()

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
    else:
        index = index + 1
        ClipDl = os.system(
            "twitch-dl download -q source --output ./preVideo/video" + str(index) + ".mp4 " + url)
        f = open("./preVideo/video" + str(index) + ".txt", "w+")
        if gameID == "417752" or gameID == "509658":
            f.write("kameto discute avec les viewers et dit des dingueries")
        else:
            f.write("kameto fait des dingueries sur " + games[gameID])
        f.close()

########################################### Lebouseuh #######################################

lebouseuhClip = "https://api.twitch.tv/helix/clips?broadcaster_id=" + lebouseuhID + "&started_at=" + \
    yesterday7RFC3339 + "&ended_at=" + todayRFC3339 + "&first=1"
lebouseuhRequest = requests.get(lebouseuhClip, headers=headers)
lebouseuhResponse = lebouseuhRequest.json()
lebouseuhResult = lebouseuhResponse.get('data')
for element in lebouseuhResult:
    if url == "":
        index = index
    else:
        index = index + 1
        ClipDl = os.system(
            "twitch-dl download -q source --output ./preVideo/video" + str(index) + ".mp4 " + url)
        f = open("./preVideo/video" + str(index) + ".txt", "w+")
        if gameID == "417752" or gameID == "509658":
            f.write("lebouseuh discute avec les viewers et dit des dingueries")
        else:
            f.write("lebouseuh fait des dingueries sur " + games[gameID])
        f.close()

########################################### Valouz ##########################################

valouzClip = "https://api.twitch.tv/helix/clips?broadcaster_id=" + valouzID + "&started_at=" + \
    yesterday7RFC3339 + "&ended_at=" + todayRFC3339 + "&first=1"
valouzRequest = requests.get(valouzClip, headers=headers)
valouzResponse = valouzRequest.json()
valouzResult = valouzResponse.get('data')
for element in valouzResult:
    url = element.get('url')
    if url == "":
        index = index
    else:
        index = index + 1
        ClipDl = os.system(
            "twitch-dl download -q source --output ./preVideo/video" + str(index) + ".mp4 " + url)
        f = open("./preVideo/video" + str(index) + ".txt", "w+")
        if gameID == "417752" or gameID == "509658":
            f.write("valouz discute avec les viewers et dit des dingueries")
        else:
            f.write("valouz fait des dingueries sur " + games[gameID])
        f.close()

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
    else:
        index = index + 1
        ClipDl = os.system(
            "twitch-dl download -q source --output ./preVideo/video" + str(index) + ".mp4 " + url)
        f = open("./preVideo/video" + str(index) + ".txt", "w+")
        if gameID == "417752" or gameID == "509658":
            f.write("domingo discute avec les viewers et dit des dingueries")
        else:
            f.write("domingo fait des dingueries sur " + games[gameID])
        f.close()

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
    else:
        index = index + 1
        ClipDl = os.system(
            "twitch-dl download -q source --output ./preVideo/video" + str(index) + ".mp4 " + url)
        f = open("./preVideo/video" + str(index) + ".txt", "w+")
        if gameID == "417752" or gameID == "509658":
            f.write("squeezie discute avec les viewers et dit des dingueries")
        else:
            f.write("squeezie fait des dingueries sur " + games[gameID])
        f.close()

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
    else:
        index = index + 1
        ClipDl = os.system(
            "twitch-dl download -q source --output ./preVideo/video" + str(index) + ".mp4 " + url)
        f = open("./preVideo/video" + str(index) + ".txt", "w+")
        if gameID == "417752" or gameID == "509658":
            f.write("ponce discute avec les viewers et dit des dingueries")
        else:
            f.write("ponce fait des dingueries sur " + games[gameID])
        f.close()

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
    else:
        index = index + 1
        ClipDl = os.system(
            "twitch-dl download -q source --output ./preVideo/video" + str(index) + ".mp4 " + url)
        f = open("./preVideo/video" + str(index) + ".txt", "w+")
        if gameID == "417752" or gameID == "509658":
            f.write("billy discute avec les viewers et dit des dingueries")
        else:
            f.write("billy fait des dingueries sur " + games[gameID])
        f.close()

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
    else:
        index = index + 1
        ClipDl = os.system(
            "twitch-dl download -q source --output ./preVideo/video" + str(index) + ".mp4 " + url)
        f = open("./preVideo/video" + str(index) + ".txt", "w+")
        if gameID == "417752" or gameID == "509658":
            f.write("amine discute avec les viewers et dit des dingueries")
        else:
            f.write("amine fait des dingueries sur " + games[gameID])
        f.close()

########################################### Krl #############################################

krlClip = "https://api.twitch.tv/helix/clips?broadcaster_id=" + krlID + "&started_at=" + \
    yesterday7RFC3339 + "&ended_at=" + todayRFC3339 + "&first=1"
krlRequest = requests.get(krlClip, headers=headers)
krlResponse = krlRequest.json()
krlResult = krlResponse.get('data')
for element in krlResult:
    url = element.get('url')
    gameID = element.get('game_id')
    if url == "":
        index = index
    else:
        index = index + 1
        ClipDl = os.system(
            "twitch-dl download -q source --output ./preVideo/video" + str(index) + ".mp4 " + url)
        f = open("./preVideo/video" + str(index) + ".txt", "w+")
        if gameID == "417752" or gameID == "509658":
            f.write("krl discute avec les viewers et dit des dingueries")
        else:
            f.write("krl fait des dingueries sur " + games[gameID])
        f.close()

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
    else:
        index = index + 1
        ClipDl = os.system(
            "twitch-dl download -q source --output ./preVideo/video" + str(index) + ".mp4 " + url)
        f = open("./preVideo/video" + str(index) + ".txt", "w+")
        if gameID == "417752" or gameID == "509658":
            f.write("melchior discute avec les viewers et dit des dingueries")
        else:
            f.write("melchior fait des dingueries sur " + games[gameID])
        f.close()

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
    else:
        index = index + 1
        ClipDl = os.system(
            "twitch-dl download -q source --output ./preVideo/video" + str(index) + ".mp4 " + url)
        f = open("./preVideo/video" + str(index) + ".txt", "w+")
        if gameID == "417752" or gameID == "509658":
            f.write("linca discute avec les viewers et dit des dingueries")
        else:
            f.write("linca fait des dingueries sur " + games[gameID])
        f.close()

########################################### Maghla ##########################################

maghlaClip = "https://api.twitch.tv/helix/clips?broadcaster_id=" + maghlaID + "&started_at=" + \
    yesterday7RFC3339 + "&ended_at=" + todayRFC3339 + "&first=1"
maghlaRequest = requests.get(maghlaClip, headers=headers)
maghlaResponse = maghlaRequest.json()
maghlaResult = maghlaResponse.get('data')
for element in maghlaResult:
    url = element.get('url')
    gameID = element.get('game_id')
    if url == "":
        index = index
    else:
        index = index + 1
        ClipDl = os.system(
            "twitch-dl download -q source --output ./preVideo/video" + str(index) + ".mp4 " + url)
        f = open("./preVideo/video" + str(index) + ".txt", "w+")
        if gameID == "417752" or gameID == "509658":
            f.write("maghla discute avec les viewers et dit des dingueries")
        else:
            f.write("maghla fait des dingueries sur " + games[gameID])
        f.close()

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
            "twitch-dl download -q source --output ./preVideo/video" + str(index) + ".mp4 " + url)
        f = open("./preVideo/video" + str(index) + ".txt", "w+")
        if gameID == "417752" or gameID == "509658":
            f.write("locklear discute avec les viewers et dit des dingueries")
        else:
            f.write("locklear fait des dingueries sur " + games[gameID])
        f.close()

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
            "twitch-dl download -q source --output ./preVideo/video" + str(index) + ".mp4 " + url)
        f = open("./preVideo/video" + str(index) + ".txt", "w+")
        if gameID == "417752" or gameID == "509658":
            f.write("lutti discute avec les viewers et dit des dingueries")
        else:
            f.write("lutti fait des dingueries sur " + games[gameID])
        f.close()

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
            "twitch-dl download -q source --output ./preVideo/video" + str(index) + ".mp4 " + url)
        f = open("./preVideo/video" + str(index) + ".txt", "w+")
        if gameID == "417752" or gameID == "509658":
            f.write("papesan discute avec les viewers et dit des dingueries")
        else:
            f.write("papesan fait des dingueries sur " + games[gameID])
        f.close()

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
            "twitch-dl download -q source --output ./preVideo/video" + str(index) + ".mp4 " + url)
        f = open("./preVideo/video" + str(index) + ".txt", "w+")
        if gameID == "417752" or gameID == "509658":
            f.write("wankil discute avec les viewers et dit des dingueries")
        else:
            f.write("wankil fait des dingueries sur " + games[gameID])
        f.close()

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
            "twitch-dl download -q source --output ./preVideo/video" + str(index) + ".mp4 " + url)
        f = open("./preVideo/video" + str(index) + ".txt", "w+")
        if gameID == "417752" or gameID == "509658":
            f.write("mickalow discute avec les viewers et dit des dingueries")
        else:
            f.write("mickalow fait des dingueries sur " + games[gameID])
        f.close()

########################################### Jeel ############################################

jeelClip = "https://api.twitch.tv/helix/clips?broadcaster_id=" + jeelID + "&started_at=" + \
    yesterday7RFC3339 + "&ended_at=" + todayRFC3339 + "&first=1"
jeelRequest = requests.get(jeelClip, headers=headers)
jeelResponse = jeelRequest.json()
jeelResult = jeelResponse.get('data')
for element in jeelResult:
    url = element.get('url')
    gameID = element.get('game_id')
    if url == "":
        index = index
    else:
        index = index + 1
        ClipDl = os.system(
            "twitch-dl download -q source --output ./preVideo/video" + str(index) + ".mp4 " + url)
        f = open("./preVideo/video" + str(index) + ".txt", "w+")
        if gameID == "417752" or gameID == "509658":
            f.write("jeel discute avec les viewers et dit des dingueries")
        else:
            f.write("jeel fait des dingueries sur " + games[gameID])
        f.close()

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
            "twitch-dl download -q source --output ./preVideo/video" + str(index) + ".mp4 " + url)
        f = open("./preVideo/video" + str(index) + ".txt", "w+")
        if gameID == "417752" or gameID == "509658":
            f.write("ultia discute avec les viewers et dit des dingueries")
        else:
            f.write("ultia fait des dingueries sur " + games[gameID])
        f.close()

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
            "twitch-dl download -q source --output ./preVideo/video" + str(index) + ".mp4 " + url)
        f = open("./preVideo/video" + str(index) + ".txt", "w+")
        if gameID == "417752" or gameID == "509658":
            f.write("sardoche discute avec les viewers et dit des dingueries")
        else:
            f.write("sardoche fait des dingueries sur " + games[gameID])
        f.close()

