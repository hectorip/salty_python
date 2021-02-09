"""
Adding intro and outro to a video using moviepy

moviepy is a library that allows you edit video directly in
Python

"""

from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# ffmpeg_extract_subclip("test.mp4", 0, 10, "cut.mp4")
sample = VideoFileClip("test.mp4")
intro = VideoFileClip("intro.mp4")

completo = concatenate_videoclips([intro, sample, intro], method="compose")
completo.write_videofile("completo.mp4", fps=30, preset="fast", threads=8)
