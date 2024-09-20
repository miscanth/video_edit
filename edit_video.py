import ffmpeg
from pathlib import Path
from constants import MAIN_FOLDER, RESULT_FOLDER
import os
from os import listdir


BASE_DIR = Path(__file__).resolve().parent
folder_dir = BASE_DIR / MAIN_FOLDER

os.makedirs(RESULT_FOLDER, exist_ok=True)




for folder in os.listdir(folder_dir):
 
    # check if the image ends with png
    """if (images.endswith(".png")):
        print(images)"""
    """for image in os.listdir(folder):
        if folder in image:"""
    (
 ffmpeg
 .input(f"{folder_dir}/{folder}/*.jpg", pattern_type='glob', framerate=24)
 .output(f"{RESULT_FOLDER}/{folder}.mp4")
 .run()
)
    



"""
(
 ffmpeg
 .input("data/Explosion Huge/*.jpg", pattern_type='glob', framerate=24) # .input('Explosion Huge %d.jpg', framerate=24)
 .output("video_result/movie_explosion.mp4")
 .run()
)"""
"""(
 ffmpeg
 .input("data/flag/*.jpg", pattern_type='glob', framerate=24) # .input('Explosion Huge %d.jpg', framerate=24)
 .output("video_result/movie_flag.mp4")
 .run()
)
(
 ffmpeg
 .input("data/blood_and_blood/*.jpg", pattern_type='glob', framerate=24) # .input('Explosion Huge %d.jpg', framerate=24)
 .output("video_result/movie_blood.mp4")
 .run()
)
(
 ffmpeg
 .input("data/flag/rain_v01/*.jpg", pattern_type='glob', framerate=24) # .input('Explosion Huge %d.jpg', framerate=24)
 .output("video_result/movie_rain.mp4")
 .run()
)
"""


"""results_dir = BASE_DIR / RESULT_FOLDER
results_dir.mkdir(exist_ok=True)"""
