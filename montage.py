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
number_video = len(os.listdir("./montage/video"))
# if number_video == 1:
#     os.system("""ffmpeg -i ./montage/video/video1.mp4 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:-1:-1:color=red" ./montage/tmp/video1.mp4""") 
#     clip1 = VideoFileClip("./montage/tmp/video1.mp4")
#     timecode = int(clip1.duration)-3
#     cutcode = int(timecode/2)
#     clip1 = clip1.subclip(0, cutcode)
#     clip1.write_videofile("./montage/result/result1.mp4")
#     clip1 = clip1.subclip(cutcode, timecode)
#     clip1.write_videofile("./montage/result/result2.mp4")

# else:

for i in range(number_video):
    os.system("""ffmpeg -i ./montage/video/video""" + str(i+1) + """.mp4 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:-1:-1:color=red" ./montage/tmp/video""" + str(i+1) +""".mp4""") 
    n = open("./montage/tmp.py","w+")
    n.write("""from moviepy.editor import *
    from os import remove
    from sys import argv
""")
    for i in range(number_video):
        n.write("clip"+ str(i+1) + """= VideoFileClip("./montage/tmp/video"""+ str(i+1)+".mp4" """")
""")

    for i in range(number_video):
        n.write("timecode"+ str(i+1) + "= int(clip"+ str(i+1)+""".duration)-3
""")

    for i in range(number_video):
        n.write("clip"+str(i+1)+"= clip"+str(i+1)+".subclip(0,timecode"+str(i+1)+""")
""")
        n.write("clip"+str(i+1)+""".write_videofile("./montage/tmp/final/video"""+str(i+1)+""".mp4")
""")
    n.write("remove(argv[0])")
    n.close()
    os.system("python3 ./montage/tmp.py")
        

    f = open("./montage/temp.py", "w+")
    f.write("""from moviepy.editor import *
    import os
    import shutil
    from os import remove
    from sys import argv
""")
    for i in range(number_video):
        f.write("clip" + str(i+1) + """ = VideoFileClip("./montage/tmp/final/video""" + str(i+1) + """.mp4")
""")
    f.write("""entre = VideoFileClip("./montage/entre/entre.mp4")
""")
    f.write("result = concatenate_videoclips([" + clip(number_video) + """])""")
    f.write("""
    result.write_videofile("./montage/result/result.mp4", fps = 30)
remove(argv[0])""")
    f.close()
    os.system("python3 ./montage/temp.py 1")
