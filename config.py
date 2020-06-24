import json

config_old_user = json.load(open('old_user_config.json'))
config_new_user = json.load(open('new_user_config.json'))

username_old=config_old_user['username']
password_old=config_old_user['password']
client_id_old = config_old_user['client_id']
client_secret_old = config_old_user['client_secret']
user_agent_old = config_old_user['user_agent']

username_new=config_new_user['username']
password_new=config_new_user['password']
client_id_new = config_new_user['client_id']
client_secret_new = config_new_user['client_secret']
user_agent_new = config_new_user['user_agent']
