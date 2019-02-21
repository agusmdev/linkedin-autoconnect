from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
"""
Automatically connect with contacts availables in "My Network"
"""


def login():
    username = ''  # -------MAIL ID----------
    password = ''  # -------PASSWORD---------

    driver = webdriver.Chrome('/usr/local/bin/chromedriver')  # path to chromedriver
    driver.get('https://linkedin.com/')

    driver.find_element_by_id('login-email').send_keys(username)
    driver.find_element_by_id('login-password').send_keys(password)
    driver.find_element_by_id('login-submit').click()
    return driver


def connector(driver):
    count = 0
    connect_list = driver.find_elements_by_class_name("artdeco-button__text")
    for list_item in connect_list:
        try:
            if (list_item.text in ["Follow", "Connect"]):
                list_item.click()
                count += 1
        except Exception:
            pass

    return count


def main():
    driver = login()
    count = 0
    """
    limit 100 connects to avoid temporary invite ban
    """
    while count < 100:
        search_url = "https://www.linkedin.com/mynetwork/"
        driver.get(search_url)
        count += connector(driver)

    driver.quit()


if __name__ == '__main__':
    main()
