from dotenv import load_dotenv
from pathlib import Path  # python3 only

def load_env():
    env_path = Path('..') / '.env'
    load_dotenv(dotenv_path=env_path)