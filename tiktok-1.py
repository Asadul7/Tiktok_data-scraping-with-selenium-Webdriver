from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='F:\chromedriver.exe')
driver.get('https://www.tiktok.com/foryou')
all_data = []
while True:
    links = []
    id = driver.find_elements(By.XPATH,'//a[@class="tiktok-1lqhxf7-StyledAuthorAnchor emt6k1z1"]')
    for profile in id:
        links.append(profile.get_attribute('href'))
    for link in links:
        driver.get(link)
        email = driver.find_element(By.XPATH,'//h2[@data-e2e="user-bio"]').text
        if '@gmail.com' in email:
            email = email.split('@gmail.com')[0].split(' ')[-1].split('\n')[-1]+'@gmail.com'
            profile_link = driver.current_url
            user_name = '@'+ driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div/div[1]/div[1]/div[2]/h2').text
            follwer = driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div/div[1]/h2[1]/div[2]/strong').text
            like = driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div/div[1]/h2[1]/div[3]/strong').text
            all_data.append([profile_link,user_name,follwer,like,email])
            print(all_data)


    #         df=pd.DataFrame(all_data, columns=['Profile link','User Name','Follwer','Like','Email'])
    #         df.to_excel('tiktok.xlsx',index=False)
    #         print('==============================')
    #         print(profile_link)
    #         print(user_name)
    #         print(follwer)
    #         print(like)
    #         print(email)
    #         print('===============================')
    # sleep(1)
    # try:
    #     dd=pd.read_excel('tiktok.xlsx')
    #     d=dd.drop_duplicates()
    #     d.to_excel('tiktok.xlsx',index=False)
    # except:
    #     pass
    # driver.get(url)
    # driver.refresh()
