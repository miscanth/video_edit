import ffmpeg
from pathlib import Path
from constants import MAIN_FOLDER, RESULT_FOLDER
import os


BASE_DIR = Path(__file__).resolve().parent
folder_dir = BASE_DIR / MAIN_FOLDER

os.makedirs(RESULT_FOLDER, exist_ok=True)


for folder in os.listdir(folder_dir):
    (
        ffmpeg
        .input(f'{folder_dir}/{folder}/*.jpg', pattern_type='glob', framerate=24)
        .output(f'{RESULT_FOLDER}/{folder}.mp4')
        .run()
    )



"""results_dir = BASE_DIR / RESULT_FOLDER
results_dir.mkdir(exist_ok=True)"""


"""if (images.endswith(".png")):
    print(images)"""
"""for image in os.listdir(folder):
    if folder in image:"""