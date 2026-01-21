import os
from pathlib import Path
from dotenv import load_dotenv

"""
Модуль конфигурации приложения.
Загружает переменные окружения из `.env` и предоставляет путь к базе данных.
"""

PRJ_ROOT = Path(__file__).resolve().parent
env_path = PRJ_ROOT / '.env'

load_dotenv(env_path)

class Config:
	"""Класс конфигурации, содержащий настройки для проекта."""
	DB_PATH = os.getenv('DB_PATH', 'my_db.db')

config = Config()