#clean up all file --> add to the script
def clip(x):
    result = ""
    for i in range(x):
        if i == x-1:
            result = result + "clip" + str(i+1)
        else: 
            result = result + "clip" + str(i+1) +", entre,  "
    return result


from moviepy.editor import *
import os
import shutil
number_video = len(os.listdir("./video"))

dir = './final'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))

dir = './tmp'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))

for i in range(number_video):
    os.system("""ffmpeg -i ./video/video""" + str(i+1) + """.mp4 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:-1:-1:color=indianred" ./tmp/video""" + str(i+1) +""".mp4""") 
os.system("taskkill /f /im ffmpeg.exe")
os.system("taskkill /f /im ffmpeg-win64-v4.2.2.exe")
n = open("./tmp.py","w+")
n.write("""from moviepy.editor import *
from os import remove
from sys import argv
screensize = (1000,1920)
""")
for i in range(number_video):
    n.write("clip"+ str(i+1) + """= VideoFileClip("./tmp/video"""+ str(i+1)+".mp4" """")
""")

for i in range(number_video):
    n.write("""with open("./videoTitles/video""" + str(i+1) + """.txt",'r') as file:
  video""" + str(i+1)+ """text = file.read().replace('\\n', '')
""")

for i in range(number_video):
    n.write("timecode"+ str(i+1) + "= int(clip"+ str(i+1)+""".duration)-3
""")

for i in range(number_video):
    n.write("clip"+str(i+1)+"= clip"+str(i+1)+".subclip(0,timecode"""+str(i+1)+""")
txt"""+str(i+1)+"=TextClip(video"+str(i+1)+"""text, font="font.ttf", fontsize = 75, color = 'white', size = screensize, method="caption")
txt"""+str(i+1)+"""=txt"""+str(i+1)+""".set_pos(('center',-600)).set_duration(clip"""+str(i+1)+""".duration)
video"""+str(i+1)+"""=CompositeVideoClip([clip"""+str(i+1)+""",txt"""+str(i+1)+"""])
""")

for i in range(number_video):
     n.write("video"+str(i+1)+""".write_videofile("./final/video"""+str(i+1)+""".mp4")
""")
n.write("remove(argv[0])")
n.close()
os.system("python tmp.py")
        

f = open("./temp.py", "w+")
f.write("""from moviepy.editor import *
import os
import shutil
from os import remove
from sys import argv
""")
for i in range(number_video):
    f.write("clip" + str(i+1) + """ = VideoFileClip("./final/video""" + str(i+1) + """.mp4")
""")
f.write("""entre = VideoFileClip("./entre/entre.mp4")
""")
f.write("result = concatenate_videoclips([" + clip(number_video) + """])""")
f.write("""
result.write_videofile("./result/result.mp4", fps = 30)
remove(argv[0])""")
f.close()
os.system("python temp.py")

os.system("python upload.py")
