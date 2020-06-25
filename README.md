## Subreddit Migrator

Reddit doesn't make it easy for you to migrate your subreddits from one account to the other but there is a workaround.

Follow the following steps to make your new account subscribe to all the subreddits that your old account was subscribed to.


1. Run this command to install all the tools required to run this tool

```
pip install -r requirements.txt
```

2. Login to your old account. Visit https://www.reddit.com/prefs/apps
![create app](./img/1.png)


3. Create an application.
 - Type of application - script
 - You can put the redirect url as http://localhost:8080
 - Rest of the things like description don't matter. Put anything there

![create app description](./img/2.png)

4. Once the application is created, copy the client id & secret id.

![getting client id & secret](./img/3.png)

5. Copy client_id & client_secret code into old_user_config.json
6. Put down your username & password in username & password section. Don't worry, the code always stay on your local machine. It is only used to authenticate your account.
7. Repeat steps 1 to 5 with your new account. Copy the client_id & client_secret code into new_user_config.json. Add your username & password of the new account there as well.
8. Run the file subreddit.py. CD into the folder containing the file & run the command -

```
python subreddit.py
```
9. All your subreddits should be copied from old account to new account.

![output](./img/4.png)
