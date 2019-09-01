from typing import List
from requests import get
import re
from manga_plugins.Provider import Provider


class BestProvider(Provider):
    chapter_idx = 0  # chapters idx storage. for example
    image_idx = 0  # images idx storage. for example
    chapters = []  # chapters storage. for example
    images = []  # images storage. for example

    def __init__(self, url: str):
        self.url = url

    def get_title(self) -> str:
        return re.search(r'<title>(.+)</title>', get(self.url).text).group(1)

    def get_chapters(self) -> List[str]:
        return ['http://example.com/manga/awesome/chapter-1.html', 'http://example.com/manga/awesome/chapter-2.html', ...]

    def get_chapter_next_page(self, html, url: str) -> str:
        chapter = self.chapters[self.chapter_idx]
        self.chapter_idx += 1
        self.image_idx = 0
        return chapter

    def get_image_next_page(self, html, url: str) -> str:
        return self.images[self.image_idx]

    def get_chapter_images(self, url: str) -> List[str]:
        return ['http://example.com/manga/awesome/image-1.jpg', 'http://example.com/manga/awesome/image-2.jpg', ...]