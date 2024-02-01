from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from pathlib import Path
def getlink(file_path) :
    if (file_path[0] == '"'):  # check if the path start with quotes mark or not
        file_path = file_path[1:-1]  # to remove quotation marks when u copy path directly
    url = "https://wetransfer.com/"
    webdriver_path = "C:\\Windows\\System32\\chromedriver.exe" # web driver location
    service = Service(webdriver_path)
    driver = webdriver.Chrome(service=service)
    driver.get(url) # open the website
    time.sleep(2) # waits for the website to load
    accept = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div[4]/button[1]')
    accept.click()
    agree = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[3]/div/div[2]/button')
    agree.click()
    driver.implicitly_wait(5)
    file_input = driver.find_element(By.XPATH, '//input[@type="file"]')
    file_input.send_keys(file_path)
    threedots = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[3]/div/div[2]/button[1]')
    threedots.click()
    time.sleep(0.5)
    uselink = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[3]/div/div[1]/div[1]/div[3]/div[1]/div/div[2]/div')
    uselink.click()
    getlink = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[3]/div/div[2]/button[2]')
    getlink.click()
    button = "link__copy" # copy link button class name
    wait = WebDriverWait(driver, 300) # this will wait for 300 sec uploading , if it takes longer u can add more
    finish = wait.until(EC.presence_of_element_located((By.CLASS_NAME, button))) # wait for the button to appear
    finish.click() # this will copy the link
    holder = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[3]/div/div[1]/div/div/div/input') # whis will locate link to print it
    link = holder.get_attribute("value")
    print("Link is copied to clipboard : ", link)
    driver.quit()
def get_file(folder) :
    folder = Path(folder)
    files = [f for f in folder.iterdir() if f.is_file()] # list of all files
    if not files:
        print('No files to upload')
        exit(-1)
    latest_file = max(files,key=lambda f: f.stat().st_ctime)
    return latest_file
folder = "C:\\Users\\abrou\\Desktop\\files to upload" ## change folder path
file_path = get_file(folder)  # path to most recent file
file_path = str(file_path)  # object to string
print(file_path)
print("file to upload : ", os.path.basename(file_path))  # file name
getlink(file_path)

