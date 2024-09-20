from constants import EXTENSION 


def is_valid_image_extension(file_name):
    """Проверяет расширение файла."""
    valid_extensions = {EXTENSION} # '.jpg', '.jpeg', '.png', '.gif', '.bmp'
    return any(file_name.lower().endswith(ext) for ext in valid_extensions)