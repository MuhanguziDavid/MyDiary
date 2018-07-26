import jwt

secret_key = 'david'

class Auth():
    @staticmethod
    def encode_auth(user_id):
        """method to generate authentication token for a user"""
        try:
            payload = {"sub":user_id}
            return jwt.encode(payload, secret_key, algorithm='HS256')
        except Exception as e:
            return e
    
    @staticmethod
    def decode_auth(auth_token):
        """method to decode the authentication token into the user id"""
        try:
            payload = jwt.decode(auth_token,secret_key)
            return payload['sub']

        except jwt.ExpiredSignatureError:
            return "Expired token, please try again"
        
        except jwt.InvalidTokenError:
            return "Invalid token, please try again"