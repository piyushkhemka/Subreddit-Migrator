## Subreddit Migrator

This allows you to migrate your subreddits from one account to the other.



1. Login to your old account. Visit https://www.reddit.com/prefs/apps
2. Create an application.
   a. Type of application - script
   b. You can put the redirect url as http://localhost:8080
   c. Rest of the things like description don't matter. Put anything there
3. Once the application is created, copy the client id & secret id.
4. Copy client_id & client_secret code into old_user_config.json
5. Put down your username & password in username & password section.
6. Repeat steps 1 to 5 with new account. Copy the client_id & client_secret code into new_user_config.json. Add your username & password of the new account there as well
7. Run the file subreddit.py.

```
python subreddit.py
```
8. All your subreddits should be copied from old account to new account.
