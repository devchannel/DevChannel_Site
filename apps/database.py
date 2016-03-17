from tinydb import TinyDB, Query

db = TinyDB('database/users.json')
User = Query()


def choose_identifier(original):
    def wrapper(**kwargs):
        if kwargs.get('slack_id'):
            kwargs['id_key'] = 'slack_id'
            kwargs['id_value'] = kwargs.get('slack_id')
            del kwargs['slack_id']
        elif kwargs.get('username'):
            kwargs['id_key'] = 'name'
            kwargs['id_value'] = kwargs.get('username')
            del kwargs['username']
        elif kwargs.get('email'):
            kwargs['id_key'] = 'email'
            kwargs['id_value'] = kwargs.get('email')
            del kwargs['email']
        else:
            return 'Please specify email, username or id'

        original(**kwargs)
    return wrapper


def insert_user(langs='', git='', timezone='', email='', username='', slack_id=''):
    data = {"skills": langs, "github": git, "time": timezone, "email": email, "name": username, 'slack_id': slack_id}
    db.insert(data)
    return 'added: {}'.format(data)


@choose_identifier
def update_user(params, id_key, id_value):
    db.update(params, User[id_key] == id_value)
    return 'updated {} with: {}'.format(id_key, params)


@choose_identifier
def get_user(id_key, id_value):
    return str(db.get(User[id_key] == id_value)) or 'User not found'


def get_all_users():
    return db.all()


@choose_identifier
def delete_user(id_key, id_value):
    db.remove(User[id_key] == id_value)
    return 'deleted: {}'.format(id_key)

if __name__ == '__main__':
    pass
