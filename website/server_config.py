import os

# github usernames
ALLOWED_USERS = {'g4s-slack', 'therightmandev'}

# github login consts
GIT_CLIENT_ID = os.environ.get('GIT_ID', '')
GIT_CLIENT_SECRET = os.environ.get('GIT_SECRET', '')

# server.py consts
SERVER_SECRET = os.environ.get('SERVER_SECRET', 'topsecret')
