import logging
import logging.config
import json
import os
from logging.handlers import RotatingFileHandler

    
class LoggingManager:
    """
    A Singleton class to encapsulate logging configuration and provide methods to manage loggers.
    """
    _instance = None  # Class-level attribute to store the single instance

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, config_file='logging_config.json', default_level=logging.INFO,
                 log_file='coreserve.log', max_bytes=10485760, backup_count=5):
        # Prevent re-initialization if already initialized
        if not hasattr(self, '_initialized'):

            self.config_file = config_file
            self.default_level = default_level
            self.log_file = log_file
            self.max_bytes = max_bytes
            self.backup_count = backup_count
            self._config_loaded = False
            self._load_logging_config()
            self._initialized = True  # Mark as initialized

    def _load_logging_config(self):
        """
        Load logging configuration from a JSON file. If the file is not found, use a basic configuration.
        """
        # Ensure logs folder exsits
        LOG_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'logs'))
        if not os.path.exists(LOG_DIR):
            os.makedirs(LOG_DIR)

        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                config = json.load(f)
            
            # Adjust the log file path to be absolute
            #   D:\\dDev\\Python\\server\\coreserve\\logs\\coreserve.log
            #   D:\\dDev\\Python\\server\\coreserve\\app\\utils\\logging_manager.py
            log_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'logs', self.log_file))
            config['handlers']['file']['filename'] = log_file_path

            logging.config.dictConfig(config)
            
            self._config_loaded = True
        else:
            print(f"Warning: Config file {self.config_file} not found. Using default configuration.")
            self._set_default_logging_config()
            self._config_loaded = True

    def _set_default_logging_config(self):
        """
        Set a default logging configuration if the config file is not found.
        """
        rotating_handler = RotatingFileHandler(
            self.log_file, maxBytes=self.max_bytes, backupCount=self.backup_count
        )
        logging.basicConfig(
            level=self.default_level,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                rotating_handler,
                logging.StreamHandler()  # Console handler
            ]
        )

    def get_logger(self, logger_name):
        """
        Get a logger with the given name.
        """
        if not self._config_loaded:
            raise RuntimeError("Logging configuration not loaded. Initialize 'LoggingManager' properly.")
        
        return logging.getLogger(logger_name)

    def set_logger_level(self, logger_name, level):
        """
        Dynamically update the log level of a specific logger.
        """
        logger = self.get_logger(logger_name)
        valid_levels = {
            'CRITICAL': logging.CRITICAL,
            'ERROR': logging.ERROR,
            'WARNING': logging.WARNING,
            'INFO': logging.INFO,
            'DEBUG': logging.DEBUG
        }
        if level.upper() in valid_levels:
            logger.setLevel(valid_levels[level.upper()])
            print(f"Logger '{logger_name}' level set to {level.upper()}")
        else:
            print(f"Invalid log level: {level}")

# Example usage
if __name__ == "__main__":
    logging_manager = LoggingManager(log_file='app.log', max_bytes=1048576, backup_count=5)  # 1 MB per file, 5 backups
    logger = logging_manager.get_logger("app.moduleA")
    logger.info("This is an info message.")
    logger.debug("This is a debug message.")
    logging_manager.set_logger_level("app.moduleA", "DEBUG")
    logger.debug("This debug message should now appear after setting the level.")
