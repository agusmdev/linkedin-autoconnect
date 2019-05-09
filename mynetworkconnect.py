from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
"""
Automatically connect with contacts availables in "My Network"
"""


class LinkedinAutoconnector:

    def __init__(self, headless=False, executable_path='/usr/local/bin/chromedriver', limit=100):
        self.headless_browser = headless
        self.driver = self._start_selenium()
        self.limit = limit
        self.wait = WebDriverWait(self.driver, 4)   # TODO

    def _start_selenium(self):
        chrome_options = Options()
        if self.headless_browser:
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')

            # replaces browser User Agent from "HeadlessChrome".
            user_agent = "Chrome"
            chrome_options.add_argument('user-agent={user_agent}'.format(user_agent=user_agent))

        return webdriver.Chrome(chrome_options=chrome_options)

    def login(self, user=None, password=None):

        self.driver.get('https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin')

        self.driver.find_element_by_id('username').send_keys(user)
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()

    def connector(self):
        count = 0
        search_url = "https://www.linkedin.com/mynetwork/"
        self.driver.get(search_url)
        connect_list = self.driver.find_elements_by_xpath('//button[@data-control-name="invite"]')
        for list_item in connect_list:
            try:
                if (list_item.text in ["Follow", "Connect"]):
                    list_item.click()
                    count += 1
            except Exception:
                pass

        return count

    def send_invites(self):
        count = 0
        while count < self.limit:
            count += self.connector()

        driver.quit()


if __name__ == '__main__':
    bot = LinkedinAutoconnector()
    bot.login("user", "pass")
    bot.send_invites()
