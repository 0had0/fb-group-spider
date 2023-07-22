import os

from scraper import CollectPosts
from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
    scraper = CollectPosts(depth=10)
    scraper.login(email=os.getenv('EMAIL'), password=os.getenv('PASSWORD'))
    scraper.collect_groups(223806401110356)
