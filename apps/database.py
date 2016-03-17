from tinydb import TinyDB, Query

db = TinyDB('database/users.json')
User = Query()


def insert_user(langs='', email='', git='', timezone='', username='', slack_id=''):
    data = {"email": email, "skills": langs, "github": git, "time": timezone, "name": username, 'slack_id': slack_id}
    db.insert(data)
    return 'added: {}'.format(data)


def update_user(params, email='', username='', slack_id=''):
    if email != '':
        db.update(params, User.email == email)
        return 'updated {} with: {}'.format(email, params)
    elif username != '':
        db.update(params, User.name == name)
        return 'updated {} with: {}'.format(username, params)
    elif slack_id != '':
        db.update(params, User.slack_id == slack_id)
        return 'updated {} with: {}'.format(slack_id, params)
    return 'Please specify email, username or id'


def get_user(email='', username='', slack_id=''):
    if email != '':
        return str(db.get(User.email == email)) or 'User not found'
    elif username != '':
        return str(db.get(User.name == username)) or 'User not found'
    elif slack_id != '':
        return str(db.get(User.slack_id == slack_id)) or 'User not found'
    return 'Please specify email, username or id'



def get_all_users():
    return db.all()


def delete_user(email='', username='', slack_id=''):
    if email != '':
        db.remove(User.email == email)
        return 'deleted: {}'.format(email)
    elif username != '':
        db.remove(User.name == username)
        return 'deleted: {}'.format(username)
    elif slack_id != '':
        db.remove(User.slack_id == slack_id)
        return 'deleted: {}'.format(slack_id)
    return 'Please specify email, username or id'


if __name__ == '__main__':
    pass
