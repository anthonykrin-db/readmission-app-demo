from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from api.auth.auth_handler import decodeJWT

# https://testdriven.io/blog/fastapi-jwt-auth/
# Add refresh tokens to automatically issue new JWTs when they expire.
# Don't know where to start? Check out this explanation by the author of Flask-JWT.

class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            #For debugging show credentials
            print("Credentials: {}".format(credentials))
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            # save credentials to state
            request.state.credentials = credentials
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> bool:
        isTokenValid: bool = False
        print("Verifying token:  {}".format(jwtoken))
        try:
            payload = decodeJWT(jwtoken)
            print("payload: {}".format(payload))
        except Exception as err:
            print("JWT Decode Error: {}".format(err))
            payload = None
        if payload:
            isTokenValid = True
        return isTokenValid

