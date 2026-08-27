from dotenv import load_dotenv

def load_env():
    load_dotenv()
    
import os
def get_key(name, default=None):
    return os.getenv(name, default)
