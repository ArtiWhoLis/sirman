import os
from pathlib import Path
from dotenv import load_dotenv

PRJ_ROOT = Path(__file__).resolve().parent

env_path = PRJ_ROOT / '.env'
#print(PRJ_ROOT, ' ', env_path)

load_dotenv(env_path)

class Config:
    LOG_FILE_PATH = os.getenv('LOG_FILE_PATH', '1.log')

config = Config()

print(config.LOG_FILE_PATH)