from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path='F:\chromedriver.exe')
driver.maximize_window()

Tiktok_profile_url_list = []
#river.get('https://www.tiktok.com/')
while True:
    driver.get('https://www.tiktok.com/')
    for i in range(1,4):
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        sleep(4)
        get_id_link = driver.find_elements("xpath","//a[@class='tiktok-1lqhxf7-StyledAuthorAnchor emt6k1z1']")
        for id in get_id_link:
            id_link = id.get_attribute('href')
            if id_link not in Tiktok_profile_url_list:
                Tiktok_profile_url_list.append(id_link)
                #print(id_link)
    #print('Code run ok.')
    # print(len(Tiktok_profile_url_list))
    # break
                for user_link in Tiktok_profile_url_list[len(Tiktok_profile_url_list)-81:]:
                        print(user_link)
                print('_____________________________________________________________')

