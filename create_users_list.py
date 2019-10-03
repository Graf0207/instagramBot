from selenium import webdriver
import time

all = 100

browser = webdriver.Chrome("D:\instaBot\chromedriver.exe")

#login to account
browser.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
time.sleep(2)
browser.find_element_by_xpath("//section/main/div/article/div/div[1]/div/form/div[2]/div/label/input").send_keys("programing0207@gmail.com")
browser.find_element_by_xpath("//section/main/div/article/div/div[1]/div/form/div[3]/div/label/input").send_keys("Oleg0207")
browser.find_element_by_xpath("//section/main/div/article/div/div[1]/div/form/div[4]").click()
time.sleep(5)

browser.get("https://www.instagram.com/vsempk/")
time.sleep(2)
browser.find_element_by_xpath("//section/main/div/header/section/ul/li[2]/a").click()
time.sleep(2)
element = browser.find_element_by_xpath("/html/body/div[3]/div/div[2]")


browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight/%s" %6, element)
time.sleep(1)
browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight/%s" %4, element)
time.sleep(1)
browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight/%s" %3, element)
time.sleep(1)
browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight/%s" %2, element)
time.sleep(1)
browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight/%s" %1.4, element)
time.sleep(1)


pers = []
t = 1
num_scroll = 0
p = 0 #Коф очікування

while len(pers) < all:
    num_scroll += 1
    browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", element)

    if num_scroll % 10 == 0:
        # Збереження юзерів у масив
        persons = browser.find_elements_by_xpath("//div[@role='dialog']/div[2]/ul/div/li/div/div/div/div/a[@title]")
        for i in range(len(persons)):
            pers.append(str(persons[i].get_attribute('href')))
    time.sleep(t)


#Очікування
if (len(pers) > (2000 + 1000*p)):
    print("\nПодождите 10 мин.")
    time.sleep(60*10)
    p += 1

# Створення фалйла зі списком юзерів
f = open("D:\instaBot\persons_list.txt", "w")
for person in pers:
    f.write(person)
    f.write("\n")