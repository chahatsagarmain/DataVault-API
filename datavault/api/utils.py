import os 
from dotenv import load_dotenv
from cryptography.fernet import Fernet
from pathlib import Path

def encrypt_password(password): 
    
    load_dotenv()
    
    key = os.getenv('ENCRYPTION_KEY')
    
    print(key)
    

def generate_key():
    key = Fernet.generate_key()
    load_dotenv()
    
    with open(".env","w+") as env:
        env.write(f'ENCRYPTION_KEY={key.decode()}')

def function():
    load_dotenv()
    print(os.environ.get('ENCRYPTION_KEY'))
    
if __name__ == "__main__":
    # generate_key()
    # function()
    