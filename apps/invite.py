import json
import time

import requests

from apps import invite_config


def send_invite(email, p_langs):
    print('ok 1')
    response = requests.post(invite_config.SLACK_INV_URL,
                             params={
                                 'token': invite_config.TOKEN,
                                 'channels': invite_config.AUTO_JOIN_CHANNELS,
                                 't': round(time.time()),
                                 'email': email,
                                 'first_name': '',
                                 'set_active': 'true',
                                 '_attempts': '1'}
                             )
    dict_data = json.loads(response.text)
    if not dict_data['ok']:
        err = dict_data['error']
        if err == 'invalid_email':
            return -1, 'Sorry, invalid email :('

        elif err == 'already_in_team':
            return 1, 'Sorry, it looks like you are already signed up\n' \
                      'You will be redirected to devchannel.slack.com'

        elif err == 'already_invited':
            return -1, "It looks like you have already been invited, please look in your mail box (and your spam box too) for an invite.\n" \
                       "If you can't find it, please contact me on:\n" \
                       "Reddit: therightman_\n" \
                       "Twitter: @therightmandev"
        else:
            return -1, dict_data['error']

    elif dict_data['ok']:
        with open("user_info.log", "a") as myfile:
                myfile.write(email + "-" + p_langs + "\n")
        return 0, 'Check your mail box :)'
