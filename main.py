import os
from pathlib import Path
import re
from typing import List
import uuid

from constants import IMAGE_EXTENSION, VIDEO_EXTENSION
import ffmpeg
from ffmpeg import Error as FFmpegError

from constants import MAIN_FOLDER, RESULT_FOLDER
from validators import is_valid_image_extension


BASE_DIR = Path(__file__).resolve().parent
data_folder = BASE_DIR / MAIN_FOLDER

# Создаём отдельный каталог для видео файлов.
os.makedirs(RESULT_FOLDER, exist_ok=True)


class Video:
    """Класс для видео объектов."""
    def __init__(self, path, sequence):
        self.path = path
        self.sequence = sequence
        self.result_name = sequence # По умолчанию равно имени секвенции


def get_sequences() -> List[str]:
    """
    Поиск среди всех изображений
    уникальных последовательностей.
    """
    video_list: List = []

    for path, folders, files in os.walk(data_folder, topdown=True):
        for folder in folders:
            name_list: List = []
            for file in os.listdir(f'{path}/{folder}'):
                if is_valid_image_extension(file):
                    num_part = ''
                    file, separator = file.split(f'.{IMAGE_EXTENSION}')
                    file = file[::-1]
                    for i in file:
                        if re.search(r'\d', i):
                            num_part += i
                        elif re.search(r'\D', i):
                            num_part += i
                            break
                    separator, name = file.split(num_part)
                    name = name[::-1]
                    if name not in name_list:
                        name_list.append(name)
            for name in name_list:
                new_video = Video(f'{path}/{folder}', name)
                video_list.append(new_video)
    return video_list


def get_duplicate_sequences(video_obj):
    """
    Проверка уникальности названий видео файлов
    и добавление идентификатора UUID к названию дубликата.
    """
    for file in os.listdir(BASE_DIR / RESULT_FOLDER):
        if f'{video_obj.sequence}.{VIDEO_EXTENSION}' == file:
                video_obj.result_name += str(uuid.uuid4())
    return video_obj


def main():
    """Основная функция монтажа видео."""
    for video in get_sequences():
        get_duplicate_sequences(video)
        try:
            (
                ffmpeg
                .input(f'{video.path}/{video.sequence}*.{IMAGE_EXTENSION}', pattern_type='glob', framerate=24)
                .output(f'{RESULT_FOLDER}/{video.result_name}.{VIDEO_EXTENSION}')
                .run()
            )
        except FFmpegError as error:
            print(error)


if __name__ == '__main__':
    main()