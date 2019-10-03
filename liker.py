from selenium import webdriver
import time


# Виключння
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException


#Параметры

# Функція перевірки елемента на сторінці

def xpath_existence (url):
    try:
        browser.find_element_by_xpath(url)
        existence = 1
    except NoSuchElementException:
        existence = 0
    return existence



browser = webdriver.Chrome("D:\instaBot\chromedriver.exe")


# Вхід в аккаунт
browser.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
time.sleep(2)
browser.find_element_by_xpath("//section/main/div/article/div/div[1]/div/form/div[2]/div/label/input").send_keys("programing0207@gmail.com")
browser.find_element_by_xpath("//section/main/div/article/div/div[1]/div/form/div[3]/div/label/input").send_keys("Oleg0207")
browser.find_element_by_xpath("//section/main/div/article/div/div[1]/div/form/div[4]").click()
time.sleep(5)


