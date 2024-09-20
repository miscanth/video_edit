![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)


# Video editing - монтаж видео из изображений
Программа на Python, которая из всех найденных секвенций из jpg файлов в папке с материалами собирает mov файлы с помощью утилиты ffmpeg.


## Возможности программы:

* Программа находит все jpg файлы во всех папках и подпапках;
* Соотносит каждый файл к своей секвенции, согласно их имени и длине номера кадра;
* Из каждой секвенции собирает mov файл и сохраняет все полученные видео файлы в отдельный каталог.


## Установка и запуск

Клонировать репозиторий и перейти в него в командной строке: 
```
git clone git@github.com:miscanth/video_edit.git
```
Создать и активировать виртуальное окружение: 
```
python3.9 -m venv venv 
```
* Если у вас Linux/macOS 

    ```
    source venv/bin/activate
    ```
* Если у вас windows 
 
    ```
    source venv/scripts/activate
    ```
В каталоге проекта при включенном виртуальном окружении обновить менеджер пакетов Package installer for Python:
```
python3.9 -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
Запустить исполнение основного модуля:
```
python3.9 main.py
```