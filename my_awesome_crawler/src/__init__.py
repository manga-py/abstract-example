from .Providers.AwesomeProvider import AwesomeProvider
from .Providers.BestProvider import BestProvider


def main():
    # I.e. the provider does not know which sites it can handle.
    provider1 = AwesomeProvider('http://example.org/manga/awesome.html')
    provider2 = BestProvider('http://example.org/manga/best.html')
    ...


if __name__ == '__main__':
    main()
