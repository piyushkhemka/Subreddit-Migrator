import config
import praw
import time

old_account = praw.Reddit(username=config.username_old,
                    password=config.password_old,
                    client_id=config.client_id_old,
                     client_secret=config.client_secret_old,
                     user_agent=config.user_agent_old)

new_account = praw.Reddit(username=config.username_new,
                    password=config.password_new,
                    client_id=config.client_id_new,
                     client_secret=config.client_secret_new,
                     user_agent=config.user_agent_new)

subreddits_old_account = list(old_account.user.subreddits(limit=None))
print(f'Old account subscribed to {len(subreddits_old_account)} subreddits.\n\n')

subreddits_new_account = list(new_account.user.subreddits(limit=None))

for counter, sub in enumerate(subreddits_old_account):
    new_account.subreddit(sub.display_name).subscribe()
    print(f'Subscribed to {sub.display_name}')
    if (counter % 100 == 0 and counter > 0):
        time.sleep(5)
        print(f'\nPhew!!! 100 subreddits subscribed already. ' +
              'Going to rest for 5 secs real quick. Nothing to worry. ' +
              'I will be back up very soon \n')
    elif (counter % 10 == 0 and counter > 0):
        time.sleep(2)
        print(f'\nResting for 2 seconds before we resume again \n')
print(f'\n\n\nAll done. Happy redditing!!!\n')
