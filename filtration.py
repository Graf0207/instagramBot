import time
from datetime import timedelta, datetime
from selenium import webdriver
import re

# Виключння
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException


browser = webdriver.Chrome("D:\instaBot\chromedriver.exe")
# Функція перевірки елемента на сторінці

def xpath_existence (url):
    try:
        browser.find_element_by_xpath(url)
        existence = 1
    except NoSuchElementException:
        existence = 0
    return existence




# параметри
days = 20 # кількість допустимих днів з останнього авторизування
acc_subscriptions = 10000000 # кількість підписників у аккаунта
publications = 3 # кількість публікацій на аккаунті

today = datetime.now()




# считування інформації зсилаючих на підписників
f = open("D:\instaBot\persons_list.txt", "r")
file_list = []
for line in f:
    file_list.append(line)
f.close()

# Обробка силок


filtered_list = []
i = 0 # Користовучі ,які підходять
j = 0 # Номер виводу в терміналі

for person in file_list:
    j += 1
    browser.get(person)
    time.sleep(1.5)


    # 1)Перевірка на закритий доступ до сторінки

    element = "//section/main/div/div[2]/article/div[1]/div/h2"
    if xpath_existence(element) == 1:
        try:
            if browser.find_element_by_xpath(element).text == "This Account is Private" or "Це закритий аккаунт":
                print(j, "Приватний аккаунт")
                continue
        except StaleElementReferenceException:
            print("Помилка, код помилки: 1")

   
   
   # 2)Перевірка на кількість підписників
    
    
    element = "//section/main/div/header/section/ul/li[3]/a/span" 
    if xpath_existence(element) == 0:
        print(j, "Помилка,код помилки: 2")
        continue
    status = browser.find_element_by_xpath(element).text
    status = re.sub(r'\s','',status) # видалення пробілів в кількості підписок
    if int(status) > acc_subscriptions:
        print(j,"У аккаунта занадто багато підписників") 
        continue 

    # Не повинно бути силки на сайт 

    element = "//section/main/div/div[1]/a"
    if xpath_existence(element) == 1:
        print(j, "Силка на сайт присутня")
        continue

    #4) Перевірка по допустимій кількості постів

    element = "//section/main/div/header/section/ul/li[1]/a/span"
    if xpath_existence(element) == 0:
        print(j, "Помилка ,код помилки: 4")
        continue
    status = browser.find_element_by_xpath(element).text
    status = re.sub(r'\s','',status) #Видалення пробілів у публікаціях
    if int(status) < publications:
        print(j, "У аккаунта недостатньо публікацій")
        continue

    #5) Перевірка на наявність автарки
    
    element = "//section/main/div/header/div/div/span/img"
    if xpath_existence(element) == 0:
        print(j,"Помилка,код помилки: 5")
        continue
    status = browser.find_element_by_xpath(element).get_attribute("src")
    if status.find("s150x150") == -1:
        print(j, "Профіль без аватарки")
        continue
    
    #6 Перевірка на дату останнього опублікованого допису

    element = "//a[contains(@href, '/p/')]"
    if xpath_existence(element) == 0:
        print(j, "Помилка,код помилки: 6")
        continue
    status = browser.find_element_by_xpath(element).get_attribute("href")
    browser.get(status)
    post_date = browser.find_element_by_xpath("//time").get_attribute("datetime")
    year = int(post_date[0:4])
    month = int(post_date[5:7])
    day = int(post_date[8:10])
    post_date = datetime(year,month,day)
    period = today - post_date
    if period.days > days:
        print(j, "Остання публікація була дуже давно")
        continue

    #6) Добавлення користувача після фільтрів

    filtered_list.append(person)
    print(j, "Доданий новий користувач", person)
    i += 1



#7)Записування в файл
f = open("D:\instaBot\philtered_persons_list.txt", 'w')
for line in filtered_list:
    f.write(line)
f.close()
print("\nДобавлено", i, "користувачі" )  


   








             