import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from helpers import getTweetIdFromUrl


class Twitter():
    '''A twitter interface to interact with twitter using a selenium driver instance'''

    TWITTER_URL = 'https://twitter.com'
    DELAY = 10
    SCROLL_DELAY = 0.5

    def __init__(self, user, password, driver):
        '''Create a twitter object given a user, password and a selenium driver'''
        self.user = user
        self.password = password
        self.driver = driver

    def login(self, login_path = 'login'):
        '''Login the selenium driver to twitter. Returns True in case of successfull login.'''
        login_path = f'{Twitter.TWITTER_URL}/{login_path}'
        self.driver.get(login_path)
        try:
            user_input = WebDriverWait(self.driver, Twitter.DELAY).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="text"]')))
        except TimeoutException:
            return False
        user_input.send_keys(self.user)
        user_input.send_keys(Keys.ENTER)
        try:
            password_input = WebDriverWait(self.driver, Twitter.DELAY).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="password"]')))
        except TimeoutException:
            return False
        password_input.send_keys(self.password)
        password_input.send_keys(Keys.ENTER)
        return True

    def scrapForHashtag(self, hashtag, query_length):
        '''Given a hashtag, use the selenium driver to return an array of the top 500 tweet ids'''
        try:
            search_input = WebDriverWait(self.driver, Twitter.DELAY).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="text"]')))
        except TimeoutException:
            return False
        
        
        search_input.send_keys(hashtag if hashtag.startswith('#') else f'#{hashtag}')
        search_input.send_keys(Keys.ENTER)

        # A little helper function, you will see it use later
        def map_a_tag_to_id(a_tag):
            try:
                href = a_tag.get_attribute('href')
                return getTweetIdFromUrl(href)
            # Prevents some weird selenium error from crashing the script
            except StaleElementReferenceException:
                return False

        # Define a post_ids set that will eventually store the post ids
        # A set here is better than an array, since we want to prevent duplicate
        post_ids = set()
        # Define a counter, to prevent inifnite searching (When no more tweets show up)
        # Allow for 5 tries
        i = 0
        while len(post_ids) < query_length and i < 5:
            time.sleep(Twitter.SCROLL_DELAY)
           
            a_tags = self.driver.find_elements(By.CSS_SELECTOR, 'a[href*="/status/"]')
            
            result = set(filter(lambda x: x, map(map_a_tag_to_id, a_tags)))
            # If more tweets show up, reset the counter
            if post_ids.union(result) != post_ids:
                i = 0
                post_ids = post_ids.union(result)
            
            # Scroll to the end of the page
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            i += 1
        return post_ids
        