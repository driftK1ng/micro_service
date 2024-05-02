import logging
import logging.handlers
from app.settings import settings

class LoggerSetup:
    def __init__(self) -> None:
        self.logger = logging.getLogger("")
        self.setup_logging()

    def setup_logging(self):
        LOG_FORMAT = "%(levelname)s - %(name)s - %(message)s - %(asctime)s"
        logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
        logging.basicConfig(level=logging.WARNING, format=LOG_FORMAT)

        formatter = logging.Formatter(LOG_FORMAT)

        console = logging.StreamHandler()
        console.setFormatter(formatter)

        if not settings.test_build:
            log_file = "logs/part.log"
            file = logging.handlers.TimedRotatingFileHandler(filename=log_file, when="midnight", backupCount=5)
            file.setFormatter(formatter)
            self.logger.addHandler(file)

        self.logger.addHandler(console)