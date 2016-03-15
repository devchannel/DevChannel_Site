from tinydb import TinyDB, Query

db = TinyDB('database/users.json')
User = Query()


def insert_user(langs='', email='', git='', timezone='', username=''):
    if username == '':
        username = email
    data = {"!skills": langs, "!github": git, "!time": timezone, "name": username}
    db.insert(data)
    return 'added: {}'.format(data)


def update_user(params, email='', username=''):
    if username == '':
        username = email
    db.update(params, User.name == username)
    return 'updated {} with: {}'.format(username, params)


def get_user(email='', username=''):
    if username == '':
        username = email
    return str(db.get(User.name == username)) or 'User not found'


def delete_user(email='', username=''):
    if username == '':
        username = email
    db.remove(User.name == username)
    return 'deleted: {}'.format(username)

if __name__ == '__main__':
    pass
