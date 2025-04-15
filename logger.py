from loguru import logger

logger.add("crawler.log", rotation="1 MB")