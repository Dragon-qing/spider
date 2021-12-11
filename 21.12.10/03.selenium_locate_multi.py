from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://bj.58.com/ershoufang/?PGTID=0d200001-0000-1d04-b922-19299535e673&ClickID=1"

driver = webdriver.Chrome()
driver.get(url)
list_el = driver.find_elements(by=By.XPATH, value='//*[@id="__layout"]/div/section/section[3]/section[1]/section[2]/div[position()<11]/a/div[2]/div[1]/div[1]/h3')
for el in list_el:
    el.click()