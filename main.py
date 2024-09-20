import ffmpeg
from pathlib import Path
from constants import MAIN_FOLDER, RESULT_FOLDER
import os


BASE_DIR = Path(__file__).resolve().parent
folder_dir = BASE_DIR / MAIN_FOLDER

os.makedirs(RESULT_FOLDER, exist_ok=True)

for path, folders, files in os.walk(folder_dir, topdown=True):
    for folder in folders:
        (
            ffmpeg
            .input(f'{path}/{folder}/*.jpg', pattern_type='glob', framerate=24)
            .output(f'{RESULT_FOLDER}/{folder}.mp4')
            .run()
        )



"""for folder in os.listdir(folder_dir):
    (
        ffmpeg
        .input(f'{folder_dir}/{folder}/*.jpg', pattern_type='glob', framerate=24)
        .output(f'{RESULT_FOLDER}/{folder}.mp4')
        .run()
    )
"""

"""for (root,dirs,files) in os.walk(folder_dir,topdown=True):
  print("Directory path: %s"%root)
  print("Directory Names: %s"%dirs)
  print("Files Names: %s"%files)"""


"""results_dir = BASE_DIR / RESULT_FOLDER
results_dir.mkdir(exist_ok=True)"""


"""if (images.endswith(".png")):
    print(images)"""
"""for image in os.listdir(folder):
    if folder in image:"""