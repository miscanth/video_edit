import ffmpeg
from pathlib import Path
from constants import MAIN_FOLDER, RESULT_FOLDER
import os, sys
import re


BASE_DIR = Path(__file__).resolve().parent
data_folder = BASE_DIR / MAIN_FOLDER

# Создаём отдельный каталог для видео файлов.
os.makedirs(RESULT_FOLDER, exist_ok=True)


video_name_list = []

for path, folders, files in os.walk(data_folder, topdown=True):
    for file in files:
        num_part = ''
        file, separator = file.split('.jpg')
        file = file[::-1]
        for i in file:
            if re.search(r'\d', i):
                num_part = num_part + i
            elif re.search(r'\D', i):
                num_part = num_part + i
                break
        separator, name = file.split(num_part)
        name = name[::-1]
        if name not in video_name_list:
            video_name_list.append(name)

print(video_name_list)

for path, folders, files in os.walk(data_folder, topdown=True):
    for folder in folders:
        for sequence in video_name_list:
                    try:
                        (
                            ffmpeg
                            .input(f'{path}/{folder}/{sequence}*.jpg', pattern_type='glob', framerate=24)
                            .output(f'{RESULT_FOLDER}/{sequence}.mp4')
                            .run()
                        )
                    except:
                         print('Oooops!')
