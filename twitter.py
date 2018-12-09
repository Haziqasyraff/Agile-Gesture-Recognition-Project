from twython import Twython, TwythonError
from random import randint
import datetime
import config
import sys


class Twitter:
    configObj = config.Config()
    twitterObj = Twython(configObj.APP_KEY, configObj.APP_SECRET, configObj.OAUTH_TOKEN, configObj.OAUTH_TOKEN_SECRET)

    def tweet(self):
        f = open('tweet_file/greetings.txt', "r")
        lines = f.readlines()
        f.close()

        count = len(lines)
        random_number = randint(0, count - 1)

        try:
            now = datetime.datetime.now()
            self.twitterObj.update_status(status=lines[random_number] + str(now))
            print("Successfully Tweeted")
        except TwythonError as e:
            print(e)

    def follow(self):
        if len(sys.argv) >= 2:
            target = sys.argv[1]
        else:
            target = input("User to follow: ")

        try:
            self.twitterObj.create_friendship(screen_name=target, follow="true")
            print("Successfully Followed")
        except TwythonError as e:
            print(e)

    def change_profile_pic(self):
        try:
            avatar = open('profile_pic/profile_pic.png', 'rb')
            self.twitterObj.update_profile_image(image=avatar)
            print("Successfully Changed")
        except TwythonError as e:
            print(e)
