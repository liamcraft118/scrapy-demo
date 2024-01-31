from enum import Enum as PythonEnum
import os

class ReactionEnum(PythonEnum):
    LOVE = "love"
    LIKE = "like"
    DISLIKE = "dislike"

class Utils():
    curr_path = os.getcwd()
    resource_path = f'{curr_path}/stardew_valley/resources/collections'
    villager_path = f'{curr_path}/stardew_valley/resources/villagers'
    host = "https://www.stardewvalleywiki.com"

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