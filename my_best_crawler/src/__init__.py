from .Crawlers.AwesomeCrawler import AwesomeCrawler
from .Crawlers.BestCrawler import BestCrawler


def main():
    # I.e. the provider does not know which sites it can handle.
    provider1 = AwesomeCrawler('http://example.org/manga/awesome.html')
    provider2 = BestCrawler('http://example.org/manga/best.html')
    ...


if __name__ == '__main__':
    main()
