from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

url = "https://wetransfer.com/"
file_path = '/uploads/affiche 1.2.png'
webdriver_path = '/chromedriver-win32/chromedriver.exe'
service = Service(webdriver_path)
driver = webdriver.Chrome(service=service)

driver.get(url)
time.sleep(2)
accept = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div[4]/button[1]')
accept.click()
agree = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[3]/div/div[2]/button')
agree.click()
driver.implicitly_wait(5)
file_input = driver.find_element(By.XPATH, '//input[@type="file"]')
file_input.send_keys(file_path)
threedots = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[3]/div/div[2]/button[1]')
threedots.click()
uselink = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[3]/div/div[1]/div[1]/div[3]/div[1]/div/div[2]/div')
uselink.click()
getlink = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[3]/div/div[2]/button[2]')
getlink.click()
time.sleep(60)
driver.implicitly_wait(10)
holder = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div/div[1]/div/div/div/input')  #lezm tlocate bl driver mich b google
link = holder.get_attribute("value")
print(link)
driver.quit()
