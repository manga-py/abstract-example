from manga_plugins.Provider import Provider
from abc import ABC
import re
from requests import get


class Crawler(Provider, ABC):
    def __init__(self, url: str):
        self.url = url

    def get_title(self) -> str:
        return re.search(r'<title>(.+)</title>', get(self.url).text).group(1)
