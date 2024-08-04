import logging
import random
import re
from pathlib import Path


class Utils:
    __colors = {
        "red": 0xFF0000,
        "orange": 0xFFA500,
        "yellow": 0xFFFF00,
        "green": 0x00FF00,
        "blue": 0x0000FF,
        "purple": 0x800080,
        "pink": 0xFFC0CB,
        "white": 0xFFFFFF,
        "dark red": 0x8B0000,
        "light coral": 0xF08080,
        "gold": 0xFFD700,
        "lime": 0x00FF00,
        "aqua": 0x00FFFF,
        "royal blue": 0x4169E1,
        "medium purple": 0x9370DB,
        "hot pink": 0xFF69B4,
        "silver": 0xC0C0C0
    }

    @staticmethod
    def list_files(directory: str) -> list[str]:
        try:
            path = Path(f"{Utils.get_bot_dir_path()}/{directory}")
            files = [f.name for f in path.iterdir() if f.is_file()]
            return files
        except FileNotFoundError:
            logging.error(f'The directory "{directory}" does not exist.')
            return []

    @staticmethod
    def get_bot_dir_path() -> str:
        path = Path(__file__).resolve()
        while path.name != "bot":
            path = path.parent
        return str(path)

    @staticmethod
    def format_num(num: int | float) -> str:
        """
            Formats number into a comma-separated format. Example:
            - 1000 -> 1,000
            - 1000000 -> 1,000,000
        """
        assert type(num) is int or type(num) is float  # DBC Design
        if num < 1000:
            return str(num)
        return re.sub(r"(\d)(?=(\d{3})+(?!\d))", r"\1,", str(num))

    @staticmethod
    def get_color(color: str) -> int:
        DEFAULT_COLOR = Utils.__colors["purple"]
        if color in Utils.__colors:
            return Utils.__colors[color]
        return DEFAULT_COLOR

    @staticmethod
    def get_random_color() -> int:
        COLOR_KEYS = tuple(Utils.__colors.keys())
        return Utils.__colors[COLOR_KEYS[random.randint(0, len(COLOR_KEYS)) - 1]]
