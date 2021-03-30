import tweepy
from random import randrange

# Authentication of Keys
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# Open text file I organized from Project Gutenberg
# https://www.gutenberg.org/files/9105/9105-h/9105-h.htm
f = open("roch.txt", "r")
a_list = f.read().strip('').split('\n')

# Filter out empty array elements from new line
# I had to do this because the text I imported uses every other line.
filter_object = filter(lambda x: x != "", a_list)
without_empty_strings = list(filter_object)

# generate random number from the length of the list
random_number = randrange(len(without_empty_strings))


# Selects a random line of text from the list and tweets it.
api.update_status(without_empty_strings[random_number])