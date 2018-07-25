from api.auth.user import User

secret_key = 'david'

users = [
    User(1, 'david', 'muha@gmail.com', '1234', '1234')
]

entries = [
    {
        "entry_id": 1,
        "user_id": 1,
        "title": "Today",
        "Description": "A memorable day"
    }
]

username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}

def authentication(username, password):
    user = username_mapping.get(username, None)
    if user and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)