# GhostCrawler

GhostCrawler is an advanced, modular, and scalable web scraping engine designed for professionals who require robust data extraction capabilities. Engineered to mimic distributed crawlers, it provides advanced identity rotation, anti-bot bypassing, and seamless integration for large-scale scraping projects.

---

## Key Features

- **Asynchronous Core**: Built on `httpx` and `aiohttp` for high-performance, non-blocking crawling.
- **Modular Middleware Pipeline**: Easily extend or customize with middleware for delays, proxy injection, error handling, and more.
- **Captcha Detection**: Integrates basic captcha detection to avoid wasting requests on blocked content.
- **Proxy and User-Agent Rotation**: Dynamically cycles proxies and user agents to avoid detection and rate limits.
- **Geo-Spoofing**: Optional support for location spoofing to target region-locked data.
- **Advanced Logging**: Structured and rotating logs using `loguru`.
- **Adaptive Retry and Backoff**: Automatic retry policies handle transient failures and adapt to rate limits.

## Typical Use Cases

- **Real Estate Data Mining**: Aggregate property listings, pricing trends, and agent data from public websites.
- **Job Market Analysis**: Scrape job boards for listings, company data, and salary insights.
- **E-commerce Intelligence**: Monitor product prices, inventory, and reviews across multiple retailers.

---

## Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/MabeyaG/ghostcrawler.git
   cd ghostcrawler
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   - Create a `.env` file in the root directory.
   - Set your proxy API and other relevant environment variables as needed.

4. **Run the Example Crawler**
   ```python
   from core.crawler import Crawler

   urls = [
       "https://www.buyrentkenya.com/property/house-for-sale",
       "https://www.buyrentkenya.com/property/apartment-for-rent"
   ]

   if __name__ == "__main__":
       crawler = Crawler(urls)
       crawler.run()
   ```

---

## Project Structure

- `core/` - Core engine modules (scheduler, request handler, etc.)
- `middleware.py` - Middleware utilities for request customization.
- `captcha_solver.py` - Captcha detection logic.
- `retry_manager.py` - Adaptive retry/backoff management.
- `logger.py` - Loguru-based logging setup.
- `config.py` - Environment and configuration management.
- `proxy/` - Proxy and user-agent pooling/rotation utilities.
- `example.py` - Minimal runnable example.
- `tests/` - Test cases for core components.

---

## Extending GhostCrawler

- **Add new middleware**: Implement your custom logic and add it to the pipeline.
- **Integrate advanced captcha solvers**: Plug in third-party services or your own models.
- **Customize scheduling**: Replace or extend the default Scheduler for specialized URL prioritization.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Disclaimer

GhostCrawler is intended for ethical and legal use only. Always ensure you comply with the terms of service of target websites and applicable laws regarding data collection.
