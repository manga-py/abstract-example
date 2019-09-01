from .Crawlers.AwesomeCrawler import AwesomeCrawler
from .Crawlers.BestCrawler import BestCrawler

from my_awesome_crawler.Providers.BestProvider import BestProvider


def main():
    # I.e. the provider does not know which sites it can handle.
    provider1 = AwesomeCrawler('http://example.org/manga/awesome.html')
    provider2 = BestCrawler('http://example.org/manga/best.html')

    awesome_provider = BestProvider('http://example.org/manga/best.html')

    provider1.get_title() -> str
    provider2.get_title() -> str
    awesome_provider.get_title() -> str

    # all methods in all providers are guaranteed to exist.
    ...


if __name__ == '__main__':
    main()
