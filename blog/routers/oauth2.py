from fastapi import Depends
from blog import token
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

def get_current_user(Token: str = Depends(oauth2_scheme)):
    return token.verify_token(Token)