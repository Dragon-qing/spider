from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.baidu.com"
driver = webdriver.Chrome()
driver.get(url)
# 通过name进行定位
# driver.find_element(by=By.NAME, value="wd").send_keys("python")
# 通过classname进行定位
# driver.find_element(by=By.CLASS_NAME, value="s_ipt").send_keys("python")
# driver.find_element(by=By.ID, value="su").click()

# driver.find_element(by=By.PARTIAL_LINK_TEXT, value="地").click()


# 目标元素在当前html中是唯一标签的时候或者是众多定位出来的标签中的一个的时候才能使用
# 返回第一个
print(driver.find_element(by=By.TAG_NAME, value="title"))