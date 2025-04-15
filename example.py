from core.crawler import Crawler

urls = [
    "https://www.buyrentkenya.com/property/house-for-sale",
    "https://www.buyrentkenya.com/property/apartment-for-rent"
]

if __name__ == "__main__":
    crawler = Crawler(urls)
    crawler.run()