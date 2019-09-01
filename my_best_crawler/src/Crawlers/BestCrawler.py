from typing import List
from . import Crawler


class BestCrawler(Crawler):
    def get_chapters(self) -> List[str]:
        return ['/manga/awesome/chapter-1.html', '/manga/awesome/chapter-2.html', ...]

    def get_chapter_next_page(self, html, url: str) -> str:
        return 'Best'

    def get_image_next_page(self, html, url: str) -> str:
        return 'Best'

    def get_chapter_images(self, url: str) -> List[str]:
        return ['/manga/awesome/image-1.jpg', '/manga/awesome/image-2.jpg', ...]