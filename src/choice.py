import datetime
import random

from config import probabilities


__author__ = 'Procrastinating CDT Students'


class PlaceChooser(object):

    WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    def __init__(self, verbose=False):
        self.VERBOSE = verbose

    def choose(self):
        today = self.WEEKDAYS[datetime.datetime.today().weekday()]
        choices = probabilities.items(today)
        rand = random.random()
        acc = 0

        if self.VERBOSE:
            for place, probability in choices:
                print("\t{0} has a probability of {1}".format(
                    place,
                    probabilities.getfloat(today, place))
                )

        for place, _ in choices:
            acc += probabilities.getfloat(today, place)

            if acc > rand:
                if self.VERBOSE:
                    print("\tThe random number is {0}".format(rand))
                    print("\tThe coin hath said {0}".format(place))

                return place
