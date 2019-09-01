from abc import ABCMeta, abstractmethod
from typing import List


class Provider(metaclass=ABCMeta):

    @abstractmethod
    def get_title(self) -> str:
        """
        return manga title
        """
        pass

    @abstractmethod
    def get_chapters(self) -> List[str]:
        """
        return chapters list
        """
        pass

    @abstractmethod
    def get_chapter_next_page(self, html, url: str) -> str:  # html type?
        """
        return next chapter url
        """
        pass

    @abstractmethod
    def get_image_next_page(self, html, url: str) -> str:  # html type?
        """
        return next image url
        """
        pass

    # def handle_error(self, state: Exception) -> None:
    #     """
    #     handle errors not need here. catch errors on your application
    #     """
    #     pass

    # def handle_image(self, image_ext: str, image_bytes: bytes) -> Optional[bytes]:
    #     """
    #     handle this on your application
    #     """
    #     pass

    @abstractmethod
    def get_chapter_images(self, url: str) -> List[str]:
        """
        return images list for chapter (example)
        """
        pass
