from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Encryption():
    def encrypt(password: str):
        return pwd_context.hash(password)
    
    def verify(encrypt_password, plain_password):
        return pwd_context.verify(plain_password, encrypt_password)