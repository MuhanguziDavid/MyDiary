import jwt

from api.auth import config

class User(object):
    def __init__(self, _id, username, email, password, confirm_password):
        self.id = _id
        self.username = username
        self.email = email
        self.password = password
        self.confirm_password = confirm_password

    @staticmethod
    def encode_auth(user_id):
        """method to generate authentication token for a user"""
        try:
            payload = {"sub":user_id}
            return jwt.encode(payload, config.secret_key, algorithm='HS256')
        except Exception as exp:
            return exp
    
    @staticmethod
    def decode_auth(auth_token):
        """method to decode the authentication token into the user id"""
        try:
            payload = jwt.decode(auth_token,config.secret_key)
            return payload['sub']

        except jwt.ExpiredSignatureError:
            return "Expired token, please try again"
        
        except jwt.InvalidTokenError:
            return "Invalid token, please try again"
    
    @staticmethod
    def create_user(cursor,name,email,password):
        db_query="INSERT INTO users (name,email,password) VALUES (%s,%s,%s)"
        cursor.execute(db_query,(name,email,password))
    
    @staticmethod   
    def get_user_by_name(dict_cursor, name):
        query_string="SELECT * FROM users WHERE name = %s "
        dict_cursor.execute(query_string,[name])
        row=dict_cursor.fetchone()
        return row