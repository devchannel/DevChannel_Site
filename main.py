from sys import argv
import requests as r
import time, json

TOKEN = ""
slackInviteUrl = "https://devchannel.slack.com/api/users.admin.invite?t=" + str(int(round(time.time() * 1000)))
autoJoinChannels = "C0H0Q0J3D,C0G16K1M2,C0H0MG1FW,C0H0MG0F6,C0H0SR40J"

alert_strt = "<script type='text/javascript'>alert(\""
alert_end = "\");</script>"

def send_invite(email, token, country, p_langs):
        data = r.post(slackInviteUrl, params={'channels': autoJoinChannels, 'email': email, 'first_name': '', 'token': token, 'set_active': 'true', '_attempts': '1'})
        dict_data = json.loads(data.content.decode('utf-8'))
        if not dict_data['ok']:
            err = dict_data['error']
            if err == 'invalid_email':
                print(alert_strt + 'Sorry, invalid email :(' + alert_end)
                print("<meta http-equiv=\"refresh\" content=\"0; url=http://thedevchannel.com/join.html\" />")
            elif err == 'already_in_team':
                print(alert_strt + 'Sorry, it looks like you are already signed up\\nYou will be redirected to devchannel.slack.com' + alert_end)
                print(print("<meta http-equiv=\"refresh\" content=\"0; url=http://devchannel.slack.com/\" />"))
            elif err == 'already_invited':
                print(alert_strt + 'It looks like you have already been invited, please look in your mail box (and your spam box too) for an invite.\\nIf you can\'t find it, please contact me on:\\nReddit: therightman_\\nTwitter: @therightmandev' + alert_end)
                print("<meta http-equiv=\"refresh\" content=\"0; url=http://thedevchannel.com/join.html\" />")
            else:
                print (alert_strt + dict_data['error'] + alert_end)
                print("<meta http-equiv=\"refresh\" content=\"0; url=http://thedevchannel.com/join.html\" />")
        elif dict_data['ok']:
            with open("user_info.log", "a") as myfile:
                    myfile.write(str(email) + "-" + str(country) + "-" + str(p_langs) + "\n")
            print(alert_strt + 'Check your mail box :)' + alert_end)
            print("<meta http-equiv=\"refresh\" content=\"0; url=http://thedevchannel.com/\"")
email, country, p_langs = argv[1], argv[2], argv[3]

if len(email) > 0 and len(country) > 0 and len(p_langs) > 0:
    send_invite(email, TOKEN, country, p_langs)
else:
    print(alert_strt + "Something\'s missing" + alert_end)
    print("<meta http-equiv=\"refresh\" content=\"0; url=http://thedevchannel.com/join.html\" />")
