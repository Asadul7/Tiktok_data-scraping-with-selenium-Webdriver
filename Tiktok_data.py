from selenium import webdriver
from time import sleep


driver = webdriver.Chrome(executable_path='F:\chromedriver.exe')
driver.maximize_window()

while True:
    list = []
    driver.get('https://www.tiktok.com/')
    scorll = driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    get_id_link = driver.find_elements("xpath","//a[@class='tiktok-1lqhxf7-StyledAuthorAnchor emt6k1z1']")
    for id in get_id_link:
        id_link = id.get_attribute('href')
        if id_link not in list:
            list.append(id_link)
        print(id_link)
        #sleep(5)

    for i in list:
        print(i)
    print('__________________________')
