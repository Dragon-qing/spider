import time
from selenium import webdriver


driver = webdriver.Chrome()
# 其中的executable_path=可以设置driver的安装路径

driver.get("https://www.baidu.com")
time.sleep(3)

driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_id("su").click()
time.sleep(6)
driver.quit()