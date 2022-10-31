from moviepy.editor import *
import os
import shutil
from os import remove
from sys import argv
clip1 = VideoFileClip("./video/video1.mp4")
entre = VideoFileClip("./entre/entre.mp4")
result = concatenate_videoclips([clip1], method="compose")
result.write_videofile("./tmp/result-nosubtitles/result.mp4", fps = 30)
remove(argv[0])