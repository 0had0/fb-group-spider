import re
import sys
import time
import json
from tqdm import tqdm

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

MOBILE_URL = 'https://m.facebook.com'


class CollectPosts(object):
    def __init__(self, ids=None, depth=1, delay=2):
        options = Options()
        options.add_argument('--headless=new')
        self.ids = ids
        self.depth = depth + 1
        self.delay = delay
        self.browser = Chrome(options=options)

    def collect_groups(self, group):
        # navigate to page
        self.browser.get(
            f'{MOBILE_URL}/groups/' + str(group) + '/')

        # Scroll down depth-times and wait delay seconds to load
        # between scrolls
        for _ in range(self.depth):
            # Scroll down to bottom
            self.browser.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            # Wait to load page
            time.sleep(self.delay)

        posts = self.browser.find_elements(By.XPATH, '//article')

        response = []
        for post in tqdm(posts):
            response.append({
                "description": post.find_element(By.XPATH, '//p').get_attribute('innerText'),
                "links": [link.get_attribute('href') for link in post.find_elements(By.XPATH, './/a')],
                "images": [{
                    "aria-label": image_tag.get_attribute("aria-label"),
                    "url": re.search("(.*)url\(\'(.*)\'\)(.*)", image_tag.get_attribute("style")).group(2) if re.search("(.*)url\(\'(.*)\'\)(.*)", image_tag.get_attribute("style")) else None,
                } if image_tag else '' for image_tag in post.find_elements(By.XPATH, './/i[@role="img"]')]
            })

        with open('posts.json', 'w') as f:
            f.write(json.dumps(response, indent=4))

    def collect(self, typ):
        if typ == "groups":
            for iden in self.ids:
                self.collect_groups(iden)
        self.browser.close()

    def login(self, email, password):
        try:
            self.browser.get(MOBILE_URL)
            self.browser.find_element(By.ID, 'email').send_keys(email)
            self.browser.find_element(By.ID, 'pass').send_keys(password)
            self.browser.find_element(By.NAME, 'login').click()
        except Exception as _:
            print("There was some error while logging in.")
            print(sys.exc_info()[0])
            exit()
