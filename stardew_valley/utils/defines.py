from enum import Enum as PythonEnum
import os

class CalendarType(PythonEnum):
    BIRTHDAY = 'birthday'
    FESTIVAL = 'festival'
    EVENT = 'event'

class SpecSeasonEnum(PythonEnum):
    Other = 'Other'

class SpecColEnum(PythonEnum):
    ANY_FISH = 'Any Fish'

class ReactionEnum(PythonEnum):
    LOVE = "love"
    LIKE = "like"
    DISLIKE = "dislike"

class CollectionType(PythonEnum):
    SHIPPED_ITEM = 'shipped_item'
    FISH = 'fish'
    ARTIFACT = 'artifact'
    MINERAL = 'mineral'
    COOKING = 'cooking'


class Utils():
    curr_path = os.getcwd()
    resource_path = f'{curr_path}/stardew_valley/resources/collections'
    villager_path = f'{curr_path}/stardew_valley/resources/villagers'
    host = "https://stardewvalleywiki.com"

    @classmethod
    def get_downloaded_htmls(cls):
        path = cls.resource_path
        file_names = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        return file_names
    
    @classmethod
    def save_html_to_file(cls, name, html, path):
        if not os.path.exists(path):
            os.makedirs(path)

        with open(f"{path}/{name}", "w", encoding="utf-8") as f:
            f.write(html)
    
    @classmethod
    def find_url(cls, name):
        root = f"{cls.curr_path}/stardew_valley/resources"
        path = f"{root}/{name}"

        if os.path.exists(path):
            return f"file://{path}"
        else:
            base_name = os.path.basename(name)
            return f"{cls.host}/{base_name}"

    @classmethod
    def save_html(cls, name, html):
        root = f"{cls.curr_path}/stardew_valley/resources"
        path = f"{root}/{name}"
        folder = os.path.dirname(path)

        if os.path.exists(path):
            return

        if not os.path.exists(folder):
            os.makedirs(folder)

        with open(path, "w", encoding="utf-8") as f:
            f.write(html)

        
