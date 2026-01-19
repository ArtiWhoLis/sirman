import os
from pathlib import Path
from dotenv import load_dotenv

PRJ_ROOT = Path(__file__).resolve().parent

env_path = PRJ_ROOT / '.env'

load_dotenv(env_path)

class Config:
    DB_PATH = os.getenv('DB_PATH', 'my_db.db')
config = Config()
