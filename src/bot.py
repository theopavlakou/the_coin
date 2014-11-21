import twitter

from config import conf
from choice import PlaceChooser

__author__ = 'Procrastinating CDT Students'


class TwitterAuthError(Exception):

    def __str__(self):
        return repr("Twitter Error: Authorisation Incorrect.")


class CDTBot():

    def __init__(self):
        self.api = None
        self.load_auth()
        self.place_chooser = PlaceChooser()

    def load_auth(self):
        """
        Loads up the API object from twitter module.
        """
        section = 'Twitter'

        consumer_key = conf.get(section, 'consumer_key')
        consumer_secret = conf.get(section, 'consumer_secret')
        access_token_key = conf.get(section, 'access_token_key')
        access_token_secret = conf.get(section, 'access_token_secret')


        api = twitter.Api(consumer_key=consumer_key,
                          consumer_secret=consumer_secret,
                          access_token_key=access_token_key,
                          access_token_secret=access_token_secret)

        if not api.VerifyCredentials():
            raise TwitterAuthError()

        self.twitter = api

    def make_choice(self):
        choice = self.place_chooser.choose()

        return ' '.join(choice.split('_')).title()

    def tweet_choice(self):
        choice = self.make_choice()
        self.twitter.PostUpdate('The coin hath chosen: {0}'.format(choice))
