import os
from pathlib import Path
import re
from typing import List

from constants import EXTENSION
import ffmpeg
from ffmpeg import Error as FFmpegError

from constants import MAIN_FOLDER, RESULT_FOLDER
from validators import is_valid_image_extension


BASE_DIR = Path(__file__).resolve().parent
data_folder = BASE_DIR / MAIN_FOLDER

# Создаём отдельный каталог для видео файлов.
os.makedirs(RESULT_FOLDER, exist_ok=True)


def find_sequences(path, folder) -> List[str]:
    """
    Поиск среди всех изображений в указанной папке
    уникальных последовательностей.
    """
    video_name_list = []

    for file in os.listdir(f'{path}/{folder}'):
        if is_valid_image_extension(file):
            num_part = ''
            file, separator = file.split(EXTENSION)
            file = file[::-1]
            for i in file:
                if re.search(r'\d', i):
                    num_part += i
                elif re.search(r'\D', i):
                    num_part += i
                    break
            separator, name = file.split(num_part)
            name = name[::-1]
            if name not in video_name_list:
                video_name_list.append(name)
    return video_name_list


def main():
    """Основная функция монтажа видео."""
    for path, folders, files in os.walk(data_folder, topdown=True):
        for folder in folders:
            for sequence in find_sequences(path, folder):
                try:
                    (
                        ffmpeg
                        .input(f'{path}/{folder}/{sequence}*{EXTENSION}', pattern_type='glob', framerate=24)
                        .output(f'{RESULT_FOLDER}/{sequence}.mp4')
                        .run()
                    )
                except FFmpegError as error:
                    print(error)


if __name__ == '__main__':
    main()
