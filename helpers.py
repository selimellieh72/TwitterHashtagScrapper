import re

def loadHashtags(file_name):
    '''Given a file name, opens the file and returns an array of hashtags'''
    with open(file_name) as f:
        return f.read().splitlines()

def loadAccount(file_name):
    '''Given a file name, opens the file and returns a tuple of a user and password'''
    with open(file_name) as f:
        file = f.read().splitlines()
        return file[0], file[1]

def getTweetIdFromUrl(tweet_url):
    '''Given a tweet url, return the corresponding tweet id'''
    result = re.search(r"/status/(\d+)", tweet_url)
    return result.group(1)

