from fastapi import APIRouter
from fastapi.responses import Response
from auth.services.authService import authService
from auth.models.userModel import User, UserLogin
from utils import utils as Utils
from fastapi import Depends, FastAPI, HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import json
import datetime
import jwt

security = HTTPBearer()
router = APIRouter()
SECRET = "S&&&p3ro9SCRETO"
ALGORITHM = "HS256"

def decodeToken(token):
    try:
        decoded = jwt.decode(token, SECRET, algorithms=ALGORITHM, options={
            "verify_exp": True,
            # Você pode adicionar outras opções de verificação aqui
        })
        return decoded
    except jwt.ExpiredSignatureError:
        return {"error": True, "message": "Expired Signature"}
    except jwt.InvalidTokenError:
        return {"error": True, "message": "Invalid Token"}

def createToken(data: dict, expiresTime = None):
    to_encode = data.copy()
    iat = datetime.datetime.utcnow() # Timestamp de quando o token foi emitido
    if expiresTime:
        exp = datetime.datetime.utcnow() + expiresTime
    else: # use 1 hour expires time
        exp = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    to_encode.update({"exp": exp})
    to_encode.update({"iat": iat})
    print("--------->", to_encode)
    encoded_jwt = jwt.encode(to_encode, SECRET, algorithm=ALGORITHM)
    return encoded_jwt

def responsePayload(content, status_code):
    return Response(content=json.dumps(content),  media_type="application/json", status_code=status_code)

@router.get("/auth/v1/user/")
def get_user(credentials: HTTPAuthorizationCredentials = Security(security)):
    if credentials:
        token = credentials.credentials
        data = decodeToken(token)
        if "error" in data:
            return data
        else:
            return {"data": data}
    else:
        raise HTTPException(status_code=401, detail="Invalid authorization credentials")

@router.post("/auth/v1/register")
def registerUser(user: User):
    if authService.findUserByUsername(str(user.username)):
        data = {
            "error": True,
            "message": "this username '"+str(user.username)+"' already exists",
            "status_code": 422
        }
        return responsePayload(content = data, status_code = data['status_code'])
    
    if authService.findUserByEmail(str(user.email)):
        data = {
            "error": True,
            "message": "this email '"+str(user.email)+"' already exists",
            "status_code": 422
        }
        return responsePayload(content = data, status_code = data['status_code'])

    createdUser = authService.createUser(user)
    data = {"data": createdUser}
    return responsePayload(content = data, status_code = 201)

@router.post("/auth/v1/login")
def login(user: UserLogin):
    user.password = Utils.hash_password(user.password)
    userInDB = authService.findUserByEmail(str(user.email))
    if userInDB:
        print(userInDB)
        if user.password == userInDB[0]['password']:
            print(userInDB[0])
            token = createToken(userInDB[0])
            print(token)
            return {"token": token}
        else:
            return {"error": True, "message": "incorrect password"}
    else:
        return {"error": True, "message": "Email not valid"}