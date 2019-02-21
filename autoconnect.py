from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
"""
remember complete fields:
username, password, msg and executable path

this script send invitations to connect with msg to avoid invitation temporary
limit
"""


def login():
    username = ''  # -------MAIL ID----------
    password = ''  # -------PASSWORD---------

    driver = webdriver.Chrome(executable_path='path/to/selenium/chrome/driver')
    driver.get('https://linkedin.com/')

    driver.find_element_by_id('login-email').send_keys(username)
    driver.find_element_by_id('login-password').send_keys(password)
    driver.find_element_by_id('login-submit').click()
    return driver


def connector(driver, msg):
    connect_list = driver.find_elements_by_class_name("search-result__actions")
    for list_item in connect_list:
        try:
            if(list_item.text == "Connect"):
                list_item.click()
                send_now_butt = driver.find_element_by_xpath('//button[@class="button-secondary-large mr1"]')
                send_now_butt.click()
                send_msg = driver.find_element_by_xpath('//*[@id="custom-message"]')
                send_msg.click()
                actions = ActionChains(driver)
                actions.send_keys(msg)
                actions.perform()
                send_now_butt = driver.find_element_by_xpath('//button[@class="button-primary-large ml1"]')
                time.sleep(1)
                send_now_butt.click()
            if (list_item.text == "Follow"):
                list_item.click()
        except:
            pass

def main():
    driver = login()
    msg = ''  # ------- MSG ----------

    for page_number in range(1, 200):
        search_url = "https://www.linkedin.com/search/results/people/?facetGeoRegion=%5B%22ar%3A0%22%5D&keywords=it%20recruiter&origin=FACETED_SEARCH&page="+str(page_number)
        driver.get(search_url)
        for i in range(1, 4):
            if(i == 1):
                driver.execute_script("window.scrollTo(0, 0);")
            else:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight/"+str(4-i)+");")
            connector(driver, msg)

    driver.quit()


if __name__ == '__main__':
    main()
