import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='library.log')
                    #encoding='utf-8')

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter('%(asctime)s -  %(message)s'))
logging.getLogger().addHandler(console_handler)

logger = logging.getLogger(__name__)
logger.debug(f"Логгер {__name__} создан")

