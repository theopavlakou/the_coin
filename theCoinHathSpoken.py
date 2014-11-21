__author__ = 's1463104'

import numpy as np
import datetime

verbose = 0
print("=== The coin shall speak, and you shall eat ===")
placeToIndex = {"Mosque Kitchen":0,
                "Noodles": 1,
                "Nile Valley":2,
                "Brazilian Pancake": 3,
                "Multi-lingual Burger Man": 4,
                "Teviot":5}
a = [(v,k) for k,v in placeToIndex.iteritems()]
indexToPlace = {}
for k,v in a:
    indexToPlace[k] = v

# A matrix of probabilities: each row is a day and the columns are indexed
# by placeToIndex. Each row must sum to 1.
probabilities = np.zeros((7,len(placeToIndex)))
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

#####################################
# Add probabilities to each place
#####################################
# Monday
probabilities[0][placeToIndex["Mosque Kitchen"]] = 0.8
probabilities[0][placeToIndex["Noodles"]] = 0.2

# Tuesday
probabilities[1][placeToIndex["Nile Valley"]] = 0.5
probabilities[1][placeToIndex["Noodles"]] = 0.5

# Wednesday
probabilities[2][placeToIndex["Teviot"]] = 0.7
probabilities[2][placeToIndex["Mosque Kitchen"]] = 0.3

# Thursday
probabilities[3][placeToIndex["Nile Valley"]] = 0.6
probabilities[3][placeToIndex["Mosque Kitchen"]] = 0.1
probabilities[3][placeToIndex["Multi-lingual Burger Man"]] = 0.3

# Friday
probabilities[4][placeToIndex["Teviot"]] = 0.7
probabilities[4][placeToIndex["Mosque Kitchen"]] = 0.3

# Saturday
probabilities[5][placeToIndex["Brazilian Pancake"]] = 0.7
probabilities[5][placeToIndex["Nile Valley"]] = 0.3

# Sunday
probabilities[6][placeToIndex["Multi-lingual Burger Man"]] = 0.7
probabilities[6][placeToIndex["Nile Valley"]] = 0.3

#####################################
# Get place
#####################################
dayIndex = datetime.datetime.today().weekday()
print("    The day is {0}.".format(weekdays[dayIndex]))

if verbose > 1:
    for i in xrange(len(probabilities[dayIndex])):
        print("    {0} has a probability of {1}".format(indexToPlace[i], probabilities[dayIndex][i]))

theRandomNumber = np.random.rand()
acc = 0
for i in xrange(len(probabilities[dayIndex])):
    acc += probabilities[dayIndex][i]
    if acc > theRandomNumber:
        if verbose > 0:
            print("    The random number is {0}".format(theRandomNumber))
        print("    The coin hath said {0}".format(indexToPlace[i]))
        break
