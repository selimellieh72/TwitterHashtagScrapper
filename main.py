from termcolor import colored
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from helpers import loadAccount, loadHashtags
from twitter import Twitter

# Defining some constants

HASHTAGS_FILE_NAME = 'hashtags.txt'
ACCOUNT_FILE_NAME = 'account.txt'
SAVE_DIR = 'results'
QUERY_LENGTH = 50

def main():
    # Load hashtags from local file
    print(colored('Loading hashtags...', 'blue'))
    hashtags = loadHashtags(HASHTAGS_FILE_NAME)
    print(colored('Done!', 'green'))

    # Load account credentials from local file
    print(colored('Loading credentials...', 'blue'))
    user, password = loadAccount(ACCOUNT_FILE_NAME)
    print(colored('Done!', 'green'))

    # Sets up web driver using Google chrome
    print(colored('Setting up web driver...', 'blue'))

    driver = webdriver.Chrome(service =Service(ChromeDriverManager().install()))
    print(colored('Done!', 'green'))

    # Create a Twitter instance
    twitter = Twitter(user, password, driver)
    print(colored('Login in...', 'blue'))
    # Logging in
    if not twitter.login():
        print(colored('Fail: Could not login', 'red'))
        return
    print(colored('Success!', 'green'))

    for hashtag in hashtags:
        # Scraping post ids for specific hashtag
        print(colored(f'Scraping post ids for hashtag: {hashtag} ', 'blue'))
        post_ids = twitter.scrapForHashtag(hashtag, QUERY_LENGTH)
        print(colored(f'Done Scrapping for hashtag: {hashtag}! (Found {len(post_ids)} posts ids)', 'green'))

        # Outputting result to a file
        with open(f'{SAVE_DIR}/{hashtag}.txt', 'w') as f:
            print(colored("Saving...", 'blue'))
            f.write(str('\n'.join(post_ids)))
            print(colored('Done!', 'green'))

main()